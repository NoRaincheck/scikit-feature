# LapScore

**Module:** `skfeature.function.similarity_based.lap_score`

## Description

LapScore (Laplacian Score for unsupervised feature selection). This algorithm evaluates features based on similarity measures between samples, making it particularly effective for high-dimensional data with small sample sizes.

## Usage

```python
from skfeature.function.similarity_based import lap_score
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Select top k features
selected_features = lap_score.select_feature(X, y, k=5)
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
