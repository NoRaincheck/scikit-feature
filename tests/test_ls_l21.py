from functools import partial

from sklearn import svm
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline

from skfeature.function.sparse_learning_based import ls_l21
from skfeature.utility.util import loadmat


def test_ls_l21():
    mat = loadmat("./data/COIL20.mat")
    X = mat["X"]  # data
    X = X.astype(float)
    y = mat["Y"]  # label
    y = y[:, 0]

    X = X[:100, :30]
    y = y[:100]
    num_fea = 10  # number of selected features
    kfold = KFold(n_splits=2, shuffle=True)

    ls_l21_partial = partial(ls_l21.proximal_gradient_descent, z=0.1)

    # build pipeline
    pipeline = Pipeline(
        [("select top k", SelectKBest(score_func=ls_l21_partial, k=num_fea)), ("linear svm", svm.LinearSVC())]
    )

    results = cross_val_score(pipeline, X, y, cv=kfold)
    print(f"Accuracy: {results.mean()}")
    assert results.mean() > 0.6
