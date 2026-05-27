# Group FS

**Module:** `skfeature.function.structure.group_fs`

## Description

Group FS (Group-based Feature Selection). These algorithms leverage the structure of the data (graphs, groups, or trees) to guide feature selection. They are particularly useful when features have inherent relationships or hierarchical structures.

## Usage

```python
from skfeature.function.structure import group_fs
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Select top k features
selected_features = group_fs.select_feature(X, y, k=5)
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
