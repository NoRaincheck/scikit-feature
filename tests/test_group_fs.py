import numpy as np
from scipy.sparse import rand

from skfeature.function.structure import group_fs


def test_group_fs():
    n_samples = 60  # specify the number of samples in the simulated data
    n_features = 100  # specify the number of features in the simulated data

    # simulate the dataset
    X = np.random.rand(n_samples, n_features)

    # simulate the feature weight
    w_orin = rand(n_features, 1, 1, random_state=0).toarray()
    w_orin[0:50] = 0

    # obtain the ground truth of the simulated dataset
    noise = np.random.rand(n_samples, 1)
    y = np.dot(X, w_orin) + 0.01 * noise
    y = y[:, 0]

    z1 = 0.5  # L1 regularization parameter
    z2 = 0.5  # L2 regularization parameter for the non-overlapping group

    # specify the group structure among features
    idx = np.array(
        [
            [1, 20, np.sqrt(20)],
            [21, 40, np.sqrt(20)],
            [41, 50, np.sqrt(10)],
            [51, 70, np.sqrt(20)],
            [71, 100, np.sqrt(30)],
        ]
    ).T
    idx = idx.astype(int)

    # perform feature selection and obtain the feature weight of all the features
    w, obj, value_gamma = group_fs.group_fs(X, y, z1, z2, idx, verbose=False)

    assert w.shape == (n_features,)
    assert np.all(np.isfinite(w))
    assert np.all(np.isfinite(value_gamma))

    # objective should decrease consistently across iterations
    active = obj > 0
    assert active.sum() > 10
    assert obj[active][0] > obj[active][-1]

    # the informative features (51-100) should be retained
    assert np.sum(np.abs(w[50:]) > 1e-4) >= 45
    # most of the uninformative features (1-50) should be pruned
    assert np.sum(np.abs(w[:50]) > 1e-4) <= 35
