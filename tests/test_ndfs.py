from functools import partial

import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.pipeline import Pipeline

from skfeature.function.sparse_learning_based import NDFS
from skfeature.utility import construct_W, unsupervised_evaluation
from skfeature.utility.util import loadmat


def test_ndfs():
    mat = loadmat("./data/COIL20.mat")
    X = mat["X"]  # data
    X = X.astype(float)
    y = mat["Y"]  # label
    y = y[:, 0]

    # construct affinity matrix
    kwargs = {"metric": "euclidean", "neighbor_mode": "knn", "weight_mode": "heat_kernel", "k": 5, "t": 1}
    W = construct_W.construct_W(X, **kwargs)

    # perform evaluation on clustering task
    num_fea = 100  # number of selected features
    num_cluster = 20  # number of clusters, it is usually set as the number of classes in the ground truth

    ndfs_partial = partial(NDFS.ndfs, W=W, n_clusters=num_cluster)
    pipeline = Pipeline([("select top k", SelectKBest(score_func=ndfs_partial, k=num_fea))])

    # set y param to be 0 to demonstrate that this works in unsupervised sense
    selected_features = pipeline.fit_transform(X, y=np.zeros(X.shape[0]))

    # perform kmeans clustering based on the selected features and repeats 20 times
    nmi_total = 0
    acc_total = 0
    for _i in range(20):
        nmi, acc = unsupervised_evaluation.evaluation(X_selected=selected_features, n_clusters=num_cluster, y=y)
        nmi_total += nmi
        acc_total += acc

    # output the average NMI and average ACC
    avg_nmi = float(nmi_total) / 20
    avg_acc = float(acc_total) / 20
    print(f"NMI: {avg_nmi}")
    print(f"ACC: {avg_acc}")

    assert avg_nmi > 0.6
    assert avg_acc > 0.55
