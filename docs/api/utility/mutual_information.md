# Mutual Information

`skfeature.utility.mutual_information`

## Description

**Mutual Information** provides discrete information-theoretic measures such as information gain, conditional entropy, and symmetrical uncertainty, which are used by filter methods like FCBF and CFS.

## Usage

```python
import numpy as np

from skfeature.utility import mutual_information

f1 = np.random.randint(0, 5, 200)
f2 = np.random.randint(0, 5, 200)
ig = mutual_information.information_gain(f1, f2)
```

## Functions

- `information_gain(f1, f2)`: compute `IG(f1, f2) = H(f1) - H(f1|f2)`
- `conditional_entropy(f1, f2)`: compute the conditional entropy `H(f1|f2)`
- `su_calculation(f1, f2)`: compute the symmetrical uncertainty between two discrete features
