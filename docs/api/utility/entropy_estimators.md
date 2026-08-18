# Entropy Estimators

`skfeature.utility.entropy_estimators`

## Description

**Entropy Estimators** provides k-nearest-neighbor based estimators of entropy, mutual information, conditional mutual information, and KL divergence. It is the numerical backend for all information-theoretic feature selection algorithms.

## Usage

```python
import numpy as np

from skfeature.utility import entropy_estimators

x = np.random.rand(200)
y = np.random.rand(200)
mi = entropy_estimators.mi(x, y)
```

## Functions

- `entropy(x, k=3, base=2)`: estimate the entropy of a continuous variable
- `mi(x, y, k=3, base=2)`: estimate the mutual information between two variables
- `cmi(x, y, z, k=3, base=2)`: estimate the conditional mutual information `I(x; y | z)`
- `kldiv(x, xp, k=3, base=2)`: estimate the KL divergence between two distributions
- `entropyd(sx, base=2)`: entropy of a discrete variable
- `midd(x, y)`: mutual information between two discrete variables
- `cmidd(x, y, z)`: conditional mutual information between discrete variables
- `hist(sx)`: histogram of a discrete variable

Based on the NPEET implementation by Greg Ver Steeg.
