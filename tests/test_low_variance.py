import numpy as np
from sklearn.datasets import make_blobs
from sklearn.pipeline import Pipeline

from skfeature.function.statistical_based import low_variance
from skfeature.utility import unsupervised_evaluation


def test_low_variance():
    # create two well-separated blobs that should be clusterable after selection
    X_blob, y_blob = make_blobs(n_samples=200, n_features=20, centers=2, cluster_std=0.6, random_state=0)
    # append constant features that a variance threshold should prune
    X_const = np.zeros((X_blob.shape[0], 10))
    X = np.column_stack([X_blob, X_const])

    threshold = 0.01
    pipeline = Pipeline([("low_variance", low_variance.low_variance_feature_selection(threshold=threshold))])
    # set y param to be 0 to demonstrate that this works in unsupervised sense
    selected_features = pipeline.fit_transform(X, y=np.zeros(X.shape[0]))

    # all constant features are removed, informative ones are kept
    assert selected_features.shape[1] == X_blob.shape[1]

    # the selected features should still recover the two clusters
    nmi, acc = unsupervised_evaluation.evaluation(X_selected=selected_features, n_clusters=2, y=y_blob)
    assert nmi > 0.8
    assert acc > 0.8