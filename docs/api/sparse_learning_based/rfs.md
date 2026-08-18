# RFS

`skfeature.function.sparse_learning_based.RFS`

## Description

**RFS** (Robust Feature Selection) jointly minimizes the l2,1-norm of both the regression error and the feature weight matrix, `min ||X' W - Y||_{2,1} + gamma ||W||_{2,1}`, making it robust to outliers and noise while selecting a shared subset of features.

## Usage

```python
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import SelectKBest

from skfeature.function.sparse_learning_based import RFS

X, y = load_breast_cancer(return_X_y=True)

selector = SelectKBest(score_func=RFS.rfs, k=10)
X_selected = selector.fit_transform(X, y)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `Y_flat`: `numpy array`, shape `(n_samples,)` — class labels
- `**kwargs`: optional `gamma` regularization parameter
- `mode`: `{"rank", "index"}`, default `"rank"`

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Nie, Feiping et al. "Efficient and robust feature selection via joint l2,1-norms minimization." NIPS 2010.
