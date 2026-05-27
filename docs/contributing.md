# Contributing

We welcome contributions to scikit-feature! This document provides guidelines for contributing.

## Development Setup

```bash
# Clone the repository
git clone https://github.com/NoRaincheck/scikit-feature.git
cd scikit-feature

# Install dependencies and package in editable mode
uv sync --group dev
uv pip install -e .
```

## Code Style

We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting:

```bash
# Format code
make format

# Check linting
make lint
```

## Testing

Tests are located in the `tests/` directory. Run them with pytest:

```bash
make test
# or
uv run pytest tests/
```

## Adding a New Algorithm

1. Create your algorithm file under the appropriate category in `skfeature/function/<category>/`
2. Follow the existing pattern for the `select_feature()` function signature
3. Add comprehensive docstrings with parameters, returns, and references
4. Write unit tests in the corresponding `tests/` directory subfolder
5. Update this documentation

## Documentation

This project uses [Docsify](https://docsify.js.org/) for documentation:

```bash
# Serve docs locally (requires a local HTTP server)
make serve-docs
```

Documentation files are markdown under `docs/`. The sidebar is configured in `docs/_sidebar.md`.

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes with tests and documentation
4. Run linting and tests (`make format && make lint && make test`)
5. Commit your changes with clear messages
6. Push to your fork and open a Pull Request

## License

By contributing, you agree that your contributions will be licensed under the GNU General Public License v2.0.
