[![PyPI - Version](https://img.shields.io/pypi/v/skfeature-chappers.svg)](https://pypi.org/project/skfeature-chappers/)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://noRaincheck.github.io/scikit-feature/)

`scikit-feature` is an open-source (GNU General Public License v2.0) feature selection repository in Python developed by Data Mining and Machine Learning Lab at Arizona State University.

It serves as a platform for facilitating feature selection application, research and comparative study. It is designed to share widely used feature selection algorithms developed in the feature selection research, and offer convenience for researchers and practitioners to perform empirical evaluation in developing new feature selection algorithms.

This fork keeps the library working against modern versions of `scikit-learn`, based on the original [scikit-feature](https://github.com/jundongl/scikit-feature) project by Jundong Li, Kewei Cheng, and Suhang Wang of the DMML Lab@ASU.

**Forked project information**

*  Project site - https://github.com/NoRaincheck/scikit-feature
*  Documentation - https://noRaincheck.github.io/scikit-feature/ (build locally via `make serve-docs`)

**Original `scikit-feature` project information**

*  Project site - https://github.com/jundongl/scikit-feature
*  Documentation - http://featureselection.asu.edu/

Installation
============

# From Sources

*  Unpack the source package somewhere
*  Run `pip install -e .` from the source distribution's top level folder

# From pip

```bash
pip install skfeature-chappers
```

## Running the Documentation Locally

The documentation is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
To view documentation locally:

```bash
make serve-docs
# Then open http://localhost:8000 in your browser
```