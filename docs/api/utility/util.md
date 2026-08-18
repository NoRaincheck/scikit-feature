# Util

`skfeature.utility.util`

## Description

**Util** contains general-purpose helpers shared across the repository, most importantly the rank conversion used to align feature rankings with scikit-learn's `SelectKBest` interface.

## Usage

```python
import numpy as np

from skfeature.utility import util

indices = np.array([3, 1, 2, 0])  # 0 is the most important feature
rank = util.reverse_argsort(indices, size=4)
```

## Functions

- `reverse_argsort(X, size=None)`: convert feature indices (0 = most important) into a rank array aligned with `sklearn.feature_selection.SelectKBest`
- `loadmat(path_to_mat)`: load a MATLAB `.mat` file into a dictionary of numpy arrays
