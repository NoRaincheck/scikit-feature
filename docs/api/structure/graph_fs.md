# Graph FS

**Module:** `skfeature.function.structure.graph_fs`

## Description

Graph FS (Graph-based Feature Selection). These algorithms leverage the structure of the data (graphs, groups, or trees) to guide feature selection. They are particularly useful when features have inherent relationships or hierarchical structures.

## Usage

```python
from skfeature.function.structure import graph_fs
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Select top k features
selected_features = graph_fs.select_feature(X, y, k=5)
print(f"Selected feature indices: {selected_features}")
```

## Parameters

- `X`: Feature matrix of shape (n_samples, n_features)
- `y`: Class labels of shape (n_samples,) or (n_samples, 1)
- `k`: Number of features to select

## Returns

- `selected_features`: Array of selected feature indices

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
