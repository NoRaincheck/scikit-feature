# MIM

**Module:** `skfeature.function.information_theoretical_based.mim`

## Description

MIM (Mutual Information Maximization) is an information-theoretic feature selection algorithm. It evaluates the relevance of features based on mutual information with the class labels, and optionally considers redundancy between selected features.

## Usage

```python
from skfeature.function.information_theoretical_based import mim
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Select top k features
selected_features = mim.select_feature(X, y, k=5)
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
