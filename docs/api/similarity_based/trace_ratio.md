# Trace Ratio

`skfeature.function.similarity_based.trace_ratio`

## Description

**Trace Ratio** performs supervised feature selection by optimizing the trace ratio criterion, `max trace(Sb) / trace(Sw)`, where `Sb` and `Sw` are the between-class and within-class scatter matrices. It supports a `fisher` or `laplacian` style for building the scatter matrices.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.function.similarity_based import trace_ratio

X, y = load_iris(return_X_y=True)

# rank features with the trace ratio criterion
score = trace_ratio.trace_ratio(X, y)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data
- `y`: `numpy array`, shape `(n_samples,)` — class labels
- `n_selected_features`: `int` — number of features to select
- `**kwargs`: `style` (`"fisher"` or `"laplacian"`) and `verbose`
- `mode`: `{{"rank", "index"}}`, default `"rank"` — `"rank"` returns an array of feature indices
  ordered by importance and aligned with `sklearn.feature_selection.SelectKBest`; `"index"` returns the
  indices of the selected features with the most important one first

## Returns

- `score`: `numpy array`, shape `(n_features,)` — ranking score of every feature, aligned with
  `sklearn.feature_selection.SelectKBest`

## References

- Original implementation from the DMML Lab@ASU Feature Selection Repository.
