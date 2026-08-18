# Graph FS

`skfeature.function.structure.graph_fs`

## Description

**Graph FS** (Graph-based Feature Selection) performs supervised feature selection by solving a sparse objective regularized over a graph that encodes relationships between features. The graph structure guides which features are kept.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.function.structure import graph_fs

X, y = load_iris(return_X_y=True)

# run graph-based feature selection (see the module docstring for parameters)
w, obj, value_gamma = graph_fs.graph_fs(X, y, lambda1=0.1, lambda2=0.1, T=5)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array`, shape `(n_samples,)` — class labels
- `**kwargs`: `lambda1`, `lambda2` regularization weights and `T` optimization iterations

## Returns

- `w`: `numpy array`, shape `(n_features,)` — learned feature weights
- `obj`: objective values across iterations
- `value_gamma`: gamma values across iterations

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
