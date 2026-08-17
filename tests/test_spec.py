from functools import partial

import numpy as np
from sklearn import svm
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline

from skfeature.function.similarity_based import SPEC
from skfeature.utility import unsupervised_evaluation
from skfeature.utility.util import loadmat


def test_spec():
    mat = loadmat("./data/COIL20.mat")
    X = mat["X"]  # data
    X = X.astype(float)
    y = mat["Y"]  # label
    y = y[:, 0]

    # perform evaluation on clustering task
    num_fea = 100  # number of selected features
    num_cluster = 20  # number of clusters, it is usually set as the number of classes in the ground truth

    pipeline = []
    spec_partial = partial(SPEC.spec, style=0)
    pipeline.append(("select top k", SelectKBest(score_func=spec_partial, k=num_fea)))
    model = Pipeline(pipeline)

    # set y param to be 0 to demonstrate that this works in unsupervised sense
    selected_features = model.fit_transform(X, y=np.zeros(X.shape[0]))

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


def test_spec_supervised():
    from sklearn.datasets import make_classification

    X, y = make_classification(n_samples=200, n_features=20, n_informative=5, n_redundant=5, n_classes=2)
    X = X.astype(float)

    num_fea = 5
    kfold = KFold(n_splits=2, shuffle=True)

    # build pipeline
    pipeline = Pipeline(
        [("select top k", SelectKBest(score_func=SPEC.spec, k=num_fea)), ("linear svm", svm.LinearSVC())]
    )

    results = cross_val_score(pipeline, X, y, cv=kfold)
    print(f"Accuracy: {results.mean()}")
    assert results.mean() > 0.5
