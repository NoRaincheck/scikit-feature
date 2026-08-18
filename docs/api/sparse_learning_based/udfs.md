# UDFS

`skfeature.function.sparse_learning_based.UDFS`

## Description

**UDFS** (Unsupervised Discriminative Feature Selection) is an unsupervised method that solves `min Tr(W' M W) + gamma ||W||_{2,1}` subject to `W'W = I`, where `M` encodes local discriminative information from the samples.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest

from skfeature.function.sparse_learning_based import UDFS

X, y = load_iris(return_X_y=True)

# rank features via SelectKBest-compatible scoring
selector = SelectKBest(score_func=UDFS.udfs, k=5)
X_selected = selector.fit_transform(X, y)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array` or `None` — optional labels (unsupervised)
- `**kwargs`: optional `gamma` regularization parameter
- `mode`: `{"rank", "index"}`, default `"rank"`

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Yang, Yi et al. "l2,1-norm regularized discriminative feature selection for unsupervised learning." IJCAI 2011.
