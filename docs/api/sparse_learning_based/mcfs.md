# MCFS

`skfeature.function.sparse_learning_based.MCFS`

## Description

**MCFS** (Multi-Cluster Feature Selection) is an unsupervised method. It first partitions the data into clusters using spectral clustering, then selects features that best represent the cluster assignments via sparse regression.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest

from skfeature.function.sparse_learning_based import MCFS

X, y = load_iris(return_X_y=True)

# rank features via SelectKBest-compatible scoring
selector = SelectKBest(score_func=MCFS.mcfs, k=5)
X_selected = selector.fit_transform(X, y)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array` or `None` — optional labels (unsupervised)
- `n_selected_features`: `int` — number of features to select
- `**kwargs`: optional `W` affinity matrix and `n_clusters`
- `mode`: `{"rank", "index"}`, default `"rank"`

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Cai, Deng, Zhang, Chiyuan, and He, Xiaofei. "Unsupervised feature selection for multi-cluster data." KDD 2010.
