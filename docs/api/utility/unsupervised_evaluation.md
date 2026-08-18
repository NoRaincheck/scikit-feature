# Unsupervised Evaluation

`skfeature.utility.unsupervised_evaluation`

## Description

**Unsupervised Evaluation** provides metrics for evaluating unsupervised feature selection results, such as clustering accuracy (after best label matching) and normalized mutual information.

## Usage

```python
import numpy as np
from sklearn.datasets import load_iris

from skfeature.utility import unsupervised_evaluation

X, y = load_iris(return_X_y=True)
acc, nmi = unsupervised_evaluation.evaluation(X, n_clusters=3, y=y)
```

## Functions

- `best_map(l1, l2)`: permute the labels of `l2` to best match `l1` (Hungarian assignment)
- `evaluation(X_selected, n_clusters, y)`: cluster the selected features and return `(accuracy, normalized_mutual_information)`
