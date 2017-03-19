Title: Setting up a DRMAA-compatible HPC cluster for reproducible research
Date: 2017-03-20
Category: Doing Science
Tags: reproducible research, python, conda, hpc, dask, sge, grid engine, mpids nld clusters, interactive computation, scripted computation
Authors: Andreas Sorge
Series: Reproducible Research Recipe

This post is about setting up a HPC cluster that runs computational tasks with
a scheduler conforming to the
[Distributed Resource Management Application API (DRMAA)][drmaa] and has a
shared filesystem (NFS) of all master and slave nodes.
This includes Grid Engine (SGE).
Out of all available Python high-level abstraction frameworks for
computational task scheduling, we choose [Dask.distributed][distributed].
Note that [Dask.distributed is not restricted to DRMAA-compatible
clusters][distributed-setups].

In order to deploy Dask on DRMAA clusters, we choose [dask-drmaa][dask-drmaa].
A prerequisite is the [python-drmaa][python-drmaa] package which interfaces
to the cluster DRMAA library.
To [setup python-drmaa][install python-drmaa], one needs to make sure that the
cluster queueing settings are sourced (environment variables ``SGE_ROOT`` and
``SGE_CELL``), as well as that the environment variable ``DRMAA_LIBRARY_PATH``
is set to the ``libdrmaa.so`` library of the system.

For example, the [settings on the MPIDS NLD clusters][andsor-bashrc] are:

```bash
source /core/ge/NLD/common/settings.sh
DRMAA_LIBRARY_PATH=/core/ge/lib/linux-x64/libdrmaa.so
export DRMAA_LIBRARY_PATH=$DRMAA_LIBRARY_PATH
```

Furthermore, and for the time being, we install a [forked version of
dask-drmaa][andsor-dask-drmaa]:

```bash
$ pip install git+https://github.com/andsor/dask-drmaa.git#egg=dask-drmaa
```

(**Note to myself: Create pull requests to the [original
dask-drmaa][dask-drmaa]**.)

An important abstraction is to **separate computation from the setup of the
computational environment**.
This means that the computational code connects to a Dask Client, but is not
responsible for spinning up the cluster.
The only parameter the computational code should take is the [``address``
parameter to connect to the scheduler][distributed-client]:

```python
# address : set either interactively or feed in as command-line argument
from dask.distributed import Client
client = Client(address)
```

*Yes, this involves one manual step in both interactive and scripted computation:
actually spinning up the dask distributed cluster and manually feeding the
``address`` parameter into the notebook or as a command-line argument to the
script.*

Both interactive and scripted computation can opt for fixed-sized clusters or
adaptive clusters.
Adaptive clusters spawn additional workers upon demand (and stop them again).
Fixed-size clusters have a fixed number of workers up and running, even though
the actual computation is long finished.
Adaptive clusters are particularly efficient if the cluster is idle.
Basically, they scale to the cluster size if necessary but keep the cluster idle
otherwise.
When the cluster is under high load and busy, it takes some time to spawn the
first workers, and in the meantime a lot more other jobs might get submitted,
further increasing the time to spawning the next workers.
Hence, under high load a fixed-sized cluster might be more efficient, as it
reserves computational resources at once.
These considerations hold for interactive computation as well as for scripted
computation.

The abstraction introduced above covers these cases, as the actual computation
only needs the ``address`` parameter and does not care about the details of the
dask distributed cluster (results will stay the same, even though the runtime of
the computation will vary).

To spin up the dask distributed cluster with dask-drmaa, either use the
command line or a Python snippet.
On the command line of the login or master node of the cluster, run

```bash
$ dask-drmaa -n 10 -q queue.q
```

for a fixed-size cluster with 10 workers running on the queue ``queue.q``.
(NB: In the [dask-drmaa fork][andsor-dask-drmaa], workers consume only one
core.)
For an adaptive cluster, simply omit the number of workers:

```bash
$ dask-drmaa -q queue.q
```

In both cases, the command will output a JSON string of the ``address``
parameter to ``stdout`` for further manual or scripted processing.

Now, we assume we have only SSH access to the cluster master or login node, and
cannot reach the Dask scheduler directly.
Luckily, we can "forward" the port the Dask scheduler listens to on the cluster
master or login node to our local host.
In order to forward the dask scheduler port to our local host, we use SSH
portforwarding:

```bash
$ ssh -N -L {port}:{hostip}:{port} {loginnode}
```

Here, substitute the scheduler ``address`` information and the SSH hostname for
the cluster master or login node.
Now, we connect to the dask scheduler on our local host with:

```python
# address is localhost:port
from dask.distributed import Client
client = Client(address)
```

The biggest caveat is that Bokeh is not forwarded this way.

Further reading and examples:

- [Custom Parallel Algorithms on a Cluster with Dask](http://matthewrocklin.com/blog/work/2017/01/24/dask-custom)

[drmaa]: https://en.wikipedia.org/wiki/DRMAA
[distributed]: https://distributed.readthedocs.io/en/latest/
[distributed-setups]: https://distributed.readthedocs.io/en/latest/setup.html
[dask-drmaa]: https://github.com/dask/dask-drmaa
[python-drmaa]: https://github.com/pygridtools/drmaa-python
[install python-drmaa]: https://github.com/pygridtools/drmaa-python#installation
[andsor-bashrc]: https://github.com/andsor/dotphiles/blob/62bdafd5ed46ab2657c8e1be9c04779d1798eb06/bashrc.d/login01#L6
[andsor-dask-drmaa]: https://github.com/andsor/dask-drmaa
[distributed-client]: http://distributed.readthedocs.io/en/latest/api.html#distributed.client.Client
