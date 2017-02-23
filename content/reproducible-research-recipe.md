Title: Ingredients for a recipe for reproducible research
Date: 2017-02-23 18:00
Category: Doing Science
Tags: reproducible research
Authors: Andreas Sorge
Series: Reproducible Research Recipe

Doing computational research in a reproducible manner requires some effort in
the first place.
The good news is, project organisation and collaboration come almost for free.

This series provides some guidance in setting up an individual or collaborative
computational research project that leads to a specific scientific output.
Project and output does not only refer to a paper, but also to other forms of
scientific output, such as presentations, a software package, or a dataset.

As in cooking, there is a plethora of possible ingredients, and a lot of
feasible choices to combine them in setting up and running a computational
research project.
This recipe makes a lot of default choices and hence, provides a working
solution.
As in cooking, the chef is free to make her own choices to refine the recipe
or adapt it to personal taste.

Specifically, the recipe employs the following ingredients:

- Operating system:
  [<i class="fa fa-linux" aria-hidden="true"></i> Ubuntu][ubuntu]
- Version control system:
  [<i class="fa fa-git" aria-hidden="true"></i> Git][git]
- Web-based version control repository:
  [<i class="fa fa-gitlab" aria-hidden="true"></i> GitLab][gitlab],
  [<i class="fa fa-github" aria-hidden="true"></i> GitHub][github]
- Scripting language:
  [<i class="fa fa-python" aria-hidden="true"></i> Python][python]
- Unit testing framework:
  [pytest][pytest]
- Property-based testing, including stateful testing:
  [Hypothesis for Python][hypothesis]
- Automate testing:
  [tox][tox]
- Versioning scheme:
  [Semantic Versioning][semver]
- Text source markup language:
  [Markdown][markdown], [reStructuredText][rst], [LaTeX][latex]
- Text document converter:
  [Pandoc][pandoc]
- Virtualization software:
  [Docker][docker]
- Reference management software:
  [Zotero][zotero]
- Task management and automation:
  [doit][doit]
- Package and environment management:
  [Conda][conda], [pip][pip]
- License:
  [<i class="fa fa-creative-commons" aria-hidden="true"></i>
  Creative Commons Attribution License][cc-by],
  [ISC License][isc]
- Interactive data science and scientific computing:
  [Project Jupyter][jupyter]
- Reproducible reporting and literate programming:
  [PythonTeX][pythontex],
  [Project Jupyter][jupyter],
  [stitch][stitch],
  [Pweave][pweave]
- Plotting:
  [HoloViews][holoviews], [Bokeh][bokeh], [Matplotlib][matplotlib]
- Technical documentation:
  [Sphinx][sphinx]
- Hosting documentation:
  [Read The Docs][rtd]
- Continuous Integration (CI):
  [GitLab CI][gitlab-ci], [Travis CI][travis-ci]
- High-Performance Computing (HPC):
  Grid Engine (SGE),
  [Dask][dask],
  Running dask on IPython parallel,
  Configuring IPython parallel on Grid Engine cluster
- Interactive High-Performance Computing (IHPC):
  Running Jupyter on a cluster node,
  [IPython Parallel][ipyparallel]
- Research data repository (with DOI):
  [Zenodo][zenodo]
- Collaborative writing and preprint publishing (with DOI):
  [Authorea][authorea]
- Persistent researcher identifier:
  [ORCID][orcid]

At the heart of the recipe is the notion of an *artifact*, as inspired by
[Bekolay (2013)][@bekolay_efficient_2013].
Note that not every ingredient applies to every type of artifact.
The following posts in this series will shed light on each ingredient as well
as on several types of artifacts, such as publication-quality research papers,
research reports, software packages and presentations.

[@bekolay_efficient_2013]: http://www.bekolay.org/scipy2013-workflow/#/

[ubuntu]: https://en.wikipedia.org/wiki/Ubuntu_(operating_system)
[git]: https://en.wikipedia.org/wiki/Git
[gitlab]: https://about.gitlab.com
[github]: https://github.com/
[python]: https://www.python.org/
[semver]: http://semver.org/
[markdown]: https://en.wikipedia.org/wiki/Markdown
[pandoc]: https://en.wikipedia.org/wiki/Pandoc
[Docker]: https://en.wikipedia.org/wiki/Docker_%28software%29
[pytest]: http://pytest.org
[hypothesis]: http://hypothesis.works/
[zotero]: https://www.zotero.org/
[doit]: http://pydoit.org/
[conda]: https://conda.io
[pip]: https://pip.pypa.io
[cc-by]: https://creativecommons.org/licenses/by/4.0/
[isc]: https://en.wikipedia.org/wiki/ISC_license
[jupyter]: http://jupyter.org
[pythontex]: http://www.ctan.org/pkg/pythontex
[stitch]: https://pystitch.github.io/
[pweave]: http://mpastell.com/pweave/
[holoviews]: http://holoviews.org
[matplotlib]: http://matplotlib.org/
[bokeh]: http://bokeh.pydata.org
[latex]: https://www.latex-project.org/
[sphinx]: http://www.sphinx-doc.org/
[rst]: https://en.wikipedia.org/wiki/ReStructuredText
[rtd]: https://readthedocs.org/
[tox]: https://tox.readthedocs.io
[gitlab-ci]: https://about.gitlab.com/gitlab-ci/
[travis-ci]: https://travis-ci.org/
[dask]: http://dask.pydata.org
[ipyparallel]: https://ipyparallel.readthedocs.io/
[zenodo]: https://zenodo.org/
[authorea]: https://www.authorea.com/
[orcid]: https://orcid.org/
