# Installation

## From pip

The simplest way to install `scikit-feature` is via pip:

```bash
pip install skfeature-chappers
```

!!! note
    The package requires **Python 3.10 or newer** and ships with `scikit-learn`,
    `pandas`, and `numpy` as runtime dependencies.

## From source

To install from the latest source code:

```bash
git clone https://github.com/NoRaincheck/scikit-feature.git
cd scikit-feature
pip install -e .
```

## Development installation

For development, use `uv` to manage dependencies:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync all dependencies (including dev and docs groups)
uv sync --group dev

# Install the package in editable mode
uv pip install -e .
```

## Running tests

After installation, run the test suite:

```bash
make test
# or
uv run pytest tests/
```

## Linting and formatting

```bash
# Format code
make format

# Check linting
make lint

# Type-check code
make typecheck
```

## Building the documentation

The documentation is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
Install the docs dependencies and build the site with:

```bash
uv sync --group docs

# Serve the site locally with live reload
make serve-docs
# open http://localhost:8000

# Build the static site into site/
make build-docs
```