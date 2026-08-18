# Contributing

We welcome contributions to `scikit-feature`! This document provides guidelines for
contributing.

## Development setup

```bash
# Clone the repository
git clone https://github.com/NoRaincheck/scikit-feature.git
cd scikit-feature

# Install dependencies and the package in editable mode
uv sync --group dev
uv pip install -e .
```

## Code style

We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting and
[ty](https://docs.astral.sh/ty/) for type checking:

```bash
# Format code
make format

# Check linting
make lint

# Type-check code
make typecheck
```

## Testing

Tests are located in the `tests/` directory, one file per algorithm. Run them with pytest:

```bash
make test
# or
uv run pytest tests/
```

## Adding a new algorithm

1.  Create your algorithm file under the appropriate category in
    `skfeature/function/<category>/`
2.  Follow the existing pattern for the scoring function signature so it stays compatible
    with `sklearn.feature_selection.SelectKBest`
3.  Add comprehensive docstrings with inputs, outputs, and references
4.  Write unit tests in the corresponding test file under `tests/`
5.  Update this documentation (see below)

## Documentation

The documentation is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
Navigation lives in `mkdocs.yml` and the pages live under `docs/`.

```bash
# Install the docs dependencies
uv sync --group docs

# Serve the docs locally with live reload
make serve-docs
# open http://localhost:8000

# Build the static site
make build-docs
```

When adding an algorithm:

-   Add a reference page under `docs/api/<category>/`
-   Link it in the category table in `docs/api/algorithms-overview.md`
-   Register it in the `nav` section of `mkdocs.yml`

## Pull request process

1.  Fork the repository
2.  Create a feature branch (`git checkout -b feature/my-feature`)
3.  Make your changes with tests and documentation
4.  Run linting, formatting, type checking, and tests
    (`make format && make lint && make typecheck && make test`)
5.  Commit your changes with clear messages
6.  Push to your fork and open a Pull Request

## License

By contributing, you agree that your contributions will be licensed under the GNU General
Public License v2.0.