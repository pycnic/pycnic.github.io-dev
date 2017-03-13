Title: Deploying Python scripts and packages internally
Date: 2017-03-13 17:00
Category: Doing Science
Tags: reproducible research, python, gold route, green route, pip, conda, pypi, web-based version control repository, git, hpc
Authors: Andreas Sorge
Series: Reproducible Research Recipe

In developing Python scripts and packages for computational research, we
distinguish two different routes to openness.
The gold standard is you develop your code in the open right away.
This means creating a public repository on a public version-control repository
service like GitHub and regularly pushing all commits there.
The green standard is to develop the code internally first and upload it later
to a public repository, before the research paper becomes available online.

On the golden route, continuous integration and deployment of scripts
and packages e.g. to PyPI is fine as the source is public anyway.
However, on the green route, the source is to remain internal for the time being
and hence, publishing the package to PyPI is not an option.
The question is, how to make sure that the developed code is well-integrated
into the Python ecosystem anyway.

Here, we restrict ourselves to the following setting:

- We do not need to build conda packages, pip packages will do.
  (We should build conda packages though as soon as we publish the source.)
- We use a private repository onto which we have command-line access
  (e.g. GitLab or GitHub with SSH key)

This means, developing a Python package, and tagging versions along, we can
install a specific version, branch, or even commit, by using
[pip with git][pip with git]:

```bash
pip install git:+ssh://SERVER/REPOSITORY-PATH[@BRANCH|VERSION|COMMIT-HASH]
```

When installing from a remote machine, e.g. a HPC cluster, one needs to register
one's SSH key from that machine to the web-based version control repository
(GitLab / GitHub).

[pip with git]: https://pip.pypa.io/en/latest/reference/pip_install/#git
