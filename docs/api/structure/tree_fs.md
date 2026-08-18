# Tree FS

`skfeature.function.structure.tree_fs`

## Description

**Tree FS** (Tree-structured Feature Selection) performs supervised feature selection with a tree-structured group lasso penalty, `min ||Xw - y||_2^2 + z * sum_i sum_j h_j^i ||w_{G_j^i}||`, where groups of features are nested in a tree hierarchy (root at level 0).

## Usage

```python
import numpy as np
from skfeature.function.structure import tree_fs

n_samples, n_features = 60, 100
X = np.random.rand(n_samples, n_features)
w_orin = np.random.rand(n_features)
y = np.dot(X, w_orin)

z = 0.5  # regularization parameter

# tree structure: rows are [start_index, end_index, level, weight]
idx = np.array(
    [[1, 50, 1, np.sqrt(50)], [51, 100, 1, np.sqrt(50)]]
).T.astype(int)

w, obj, value_gamma = tree_fs.tree_fs(X, y, z, idx)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array`, shape `(n_samples,)` — target values
- `z`: `float` — regularization parameter
- `idx`: `numpy array` — tree structure, each column `[start, end, level, weight]`
- `**kwargs`: optional `verbose`

## Returns

- `w`: `numpy array`, shape `(n_features,)` — learned feature weights
- `obj`: objective values across iterations
- `value_gamma`: gamma values across iterations

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
