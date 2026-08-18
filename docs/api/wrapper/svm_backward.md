# SVM Backward

`skfeature.function.wrapper.svm_backward`

## Description

**SVM Backward** is a wrapper method that starts from the full feature set and greedily removes the least useful feature at each step, based on the cross-validated accuracy of a Support Vector Machine.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.function.wrapper import svm_backward

X, y = load_iris(return_X_y=True)

# rank features by cross-validated classifier performance
score = svm_backward.svm_backward(X, y)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array`, shape `(n_samples,)` — class labels
- `n_selected_features`: `int` — number of features to select
- `mode`: `{"rank", "index"}`, default `"rank"`

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
