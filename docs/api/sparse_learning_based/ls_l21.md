# ls_l21

`skfeature.function.sparse_learning_based.ls_l21`

## Description

**ls_l21** (least squares with l2,1-norm) performs supervised sparse feature selection by minimizing a squared-loss objective regularized by the l2,1 norm, `min ||XW - Y||_F^2 + z ||W||_{2,1}`. The l2,1 norm drives rows of the weight matrix to zero, performing joint feature selection across all targets.

## Usage

```python
import numpy as np
from functools import partial

from sklearn.feature_selection import SelectKBest

from skfeature.function.sparse_learning_based import ls_l21

# y is expected as a one-hot encoded label matrix
X = np.random.rand(200, 100)
y = np.random.randint(0, 2, 200)

score_func = partial(ls_l21.proximal_gradient_descent, z=0.1)
selector = SelectKBest(score_func=score_func, k=10)
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
