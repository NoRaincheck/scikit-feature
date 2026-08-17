import random

import numpy as np
import pytest


@pytest.fixture(autouse=True)
def _reset_random_seed():
    """Pin the global PRNGs so tests are deterministic and order-independent."""
    np.random.seed(0)
    random.seed(0)