# Group FS

`skfeature.function.structure.group_fs`

## Description

**Group FS** (Group-based Feature Selection) performs supervised sparse group feature selection, `min ||Xw - y||_2^2 + z1 ||w||_1 + z2 * sum_i h_i ||w_{G_i}||`, where features are organized into non-overlapping groups and both sparsity and group structure are enforced.

## Usage

```python
import numpy as np
from skfeature.function.structure import group_fs

n_samples, n_features = 60, 100
X = np.random.rand(n_samples, n_features)
w_orin = np.random.rand(n_features)
y = np.dot(X, w_orin)

z1 = 0.5  # L1 regularization parameter
z2 = 0.5  # group regularization parameter

# group structure: rows are [start_index, end_index, weight]
idx = np.array(
    [[1, 20, np.sqrt(20)], [21, 40, np.sqrt(20)], [41, 50, np.sqrt(10)]]
).T.astype(int)

w, obj, value_gamma = group_fs.group_fs(X, y, z1, z2, idx)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array`, shape `(n_samples,)` — target values
- `z1`: `float` — L1 regularization parameter
- `z2`: `float` — group (L2) regularization parameter
- `idx`: `numpy array` — group structure, each column `[start, end, weight]`
- `**kwargs`: optional `verbose`

## Returns

- `w`: `numpy array`, shape `(n_features,)` — learned feature weights
- `obj`: objective values across iterations
- `value_gamma`: gamma values across iterations

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
