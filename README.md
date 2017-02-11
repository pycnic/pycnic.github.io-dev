# pycnic.github.io-dev
Development and sources for the Pycnic Blog

The Pycnic blog is run with [Pelican on Github Pages][1].
The [pycnic.github.io][2] repository stores the static sites generated by
Pelican.

## Setup

Step 1: Clone the repository (including submodules):

```bash
$ git clone --recursive git@github.com:pycnic/pycnic.github.io-dev.git pycnic-blog
$ cd pycnic-blog
$ git submodule update --init --recursive
```

Step 2: Set up the environment with conda:
```bash
$ conda env create -f environment.yml
```

## Write posts

Step 1: Activate the environment:
```bash
$ source activate pycnic-blog
```

Step 2: [Add your content to the ``content`` folder.](http://docs.getpelican.com/en/stable/content.html)

Step 3: Check locally:
```bash
$ make devserver
```
Navigate to http://localhost:8000 to inspect your changes.

Step 4: If satisfied, commit and push added or changed sources in the ``content`` directory.

## Publish

**CAUTION Step 0: Do not forget to commit and push your changes to this source repository (see Step 4 above).**
Otherwise, next time your collaborator publishes her new posts, it will not contain your changes / additions!

Step 1: Activate the environment:
```bash
$ source activate pycnic-blog
```

Step 2: Commit the output to the gh-pages branch and push it to the Github Pages http://github.com/pycnic/pycnic.github.io repository
```bash
$ make github
```

Step 3: Check website at http://blog.pycnic.org!

## License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
  <img
    alt="Creative Commons License"
    style="border-width:0"
    src="https://i.creativecommons.org/l/by/4.0/88x31.png"
  />
</a>
<br />
This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
  Creative Commons Attribution 4.0 International License
</a>.

[1]: https://fedoramagazine.org/make-github-pages-blog-with-pelican/
[2]: https://github.com/pycnic/pycnic.github.io
