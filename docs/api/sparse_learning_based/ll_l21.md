# Ll_l21

**Module:** `skfeature.function.sparse_learning_based.ll_l21`

## Description

Ll_l21 (L1,2 Norm Regularization for feature selection). This algorithm uses sparse representation with L21 norm regularization to select features, making it robust to outliers and noise in the data.

## Usage

```python
from skfeature.function.sparse_learning_based import ll_l21
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Select top k features
selected_features = ll_l21.select_feature(X, y, k=5)
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
