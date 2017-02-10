# pycnic.github.io-dev
Development and sources for the Pycnic Blog

The Pycnic blog is run with [Pelican on Github Pages][1].
The [pycnic.github.io][2] repository stores the static sites generated by
Pelican.

## Setup

1. Clone the repository:
   ```bash
   $ git clone git@github.com:pycnic/pycnic.github.io-dev.git pycnic-blog
   $ cd pycnic-blog
   ```
2. Set up the environment with conda:
   ```bash
   $ conda env create -f environment.yml
   $ source activate pycnic-blog
   ```

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
