# SVM Backward

**Module:** `skfeature.function.wrapper.svm_backward`

## Description

SVM Backward (SVM-based Backward Elimination). Wrapper methods use a predetermined classifier to evaluate subsets of features. They generally provide better performance than filter methods but at higher computational cost.

## Usage

```python
from skfeature.function.wrapper import svm_backward
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Select top k features
selected_features = svm_backward.select_feature(X, y, k=5)
print(f"Selected feature indices: {selected_features}")
```

## Parameters

- `X`: Feature matrix of shape (n_samples, n_features)
- `y`: Class labels of shape (n_samples,) or (n_samples, 1)
- `k`: Number of features to select

## Returns

- `selected_features`: Array of selected feature indices

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
