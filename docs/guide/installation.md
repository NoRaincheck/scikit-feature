# Installation

## From pip

The simplest way to install `scikit-feature` is via pip:

```bash
pip install skfeature-chappers
```

## From Source

To install from the latest source code:

```bash
git clone https://github.com/HeardACat/scikit-feature.git
cd scikit-feature
pip install -e .
```

## Development Installation

For development, use `uv` to manage dependencies:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync all dependencies (including dev)
uv sync --group dev

# Install the package in editable mode
uv pip install -e .
```

## Dependencies

- Python >= 3.9
- scikit-learn
- pandas
- numpy

## Running Tests

After installation, run the test suite:

```bash
pytest tests/
```

Or with `uv`:

```bash
make test
```

## Linting and Formatting

```bash
# Format code
make format

# Check linting
make lint
```
