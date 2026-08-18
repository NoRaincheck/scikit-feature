# SVM Forward

`skfeature.function.wrapper.svm_forward`

## Description

**SVM Forward** is a wrapper method that greedily adds features to a subset based on the cross-validated accuracy of a Support Vector Machine trained on the current subset.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.function.wrapper import svm_forward

X, y = load_iris(return_X_y=True)

# rank features by cross-validated classifier performance
score = svm_forward.svm_forward(X, y)
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
