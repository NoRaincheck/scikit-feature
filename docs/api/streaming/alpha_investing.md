# Alpha Investing

`skfeature.function.streaming.alpha_investing`

## Description

**Alpha Investing** is a streamwise (online) feature selection method. Features arrive one at a time and are accepted or rejected on the fly using the alpha-investing rule with a wealth parameter, suitable for binary and univariate regression problems.

## Usage

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

from skfeature.function.streaming import alpha_investing

X, y = make_classification(n_samples=200, n_features=20, n_informative=5)
y = y.astype(float)

pipeline = Pipeline(
    [
        ("alphainvesting", alpha_investing.AlphaInvesting(w0=0.05, dw=0.05)),
        ("svm", SVC()),
    ]
)
pipeline.fit(X, y)
```

## Parameters

- `X`: `numpy array`, shape `(n_samples, n_features)` — input data, one feature per time step
- `y`: `numpy array`, shape `(n_samples,)` — class labels or regression target
- `w0`: `float` — initial wealth
- `dw`: `float` — wealth increment

## Returns

- The module also exposes the `AlphaInvesting` class, a `sklearn.base.TransformerMixin` for use inside scikit-learn pipelines.

## References

- Zhou, Jing, Foster, Dean P., Stine, Robert A., and Ungar, Lyle H. "Streamwise feature selection." JMLR 2006.
