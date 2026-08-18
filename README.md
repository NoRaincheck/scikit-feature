`scikit-feature` is an open-source (GNU General Public License v2.0) feature selection repository in Python developed by Data Mining and Machine Learning Lab at Arizona State University.

It serves as a platform for facilitating feature selection application, research and comparative study. It is designed to share widely used feature selection algorithms developed in the feature selection research, and offer convenience for researchers and practitioners to perform empirical evaluation in developing new feature selection algorithms.

This is may or may not be a temporary fork of the original repository as development seems to have stalled and various modules have been depreciated due to updates to `scikit-learn`. I will see if should get reintegrated back into the original project if it ever gets revived again.

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