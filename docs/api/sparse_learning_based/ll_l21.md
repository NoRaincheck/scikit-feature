# ll_l21

`skfeature.function.sparse_learning_based.ll_l21`

## Description

**ll_l21** (logistic loss with l2,1-norm) performs supervised sparse feature selection by minimizing a logistic loss regularized by the l2,1 norm, `min sum_i log(1 + exp(-y_i (w' x_i + c))) + z ||W||_{2,1}`. The l2,1 norm encourages row sparsity so that irrelevant features receive zero weight.

## Usage

```python
import numpy as np
from functools import partial

from sklearn.feature_selection import SelectKBest

from skfeature.function.sparse_learning_based import ll_l21
from skfeature.utility.util import loadmat

# binary labels are expected as a one-hot encoded matrix
mat = loadmat("./data/COIL20.mat")
X = mat["X"].astype(float)
y = mat["Y"][:, 0]

score_func = partial(ll_l21.proximal_gradient_descent, z=0.1)
selector = SelectKBest(score_func=score_func, k=100)
X_selected = selector.fit_transform(X, y)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `Y_flat`: `numpy array` — class labels
- `z`: `float` — regularization parameter controlling the l2,1-norm penalty
- `mode`: `{"rank", "index"}`, default `"rank"`
- `**kwargs`: additional parameters

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
