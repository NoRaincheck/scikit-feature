from sklearn import svm
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline

from skfeature.function.information_theoretical_based import CMIM
from skfeature.utility.util import loadmat


def test_cmim():
    mat = loadmat("./data/colon.mat")
    X = mat["X"]  # data
    X = X.astype(float)
    y = mat["Y"]  # label
    y = y[:, 0]

    # reduce the sample to speed up the test
    X = X[:, :30]
    num_fea = 10  # number of selected features
    kfold = KFold(n_splits=2, shuffle=True)

    # build pipeline
    pipeline = Pipeline(
        [("select top k", SelectKBest(score_func=CMIM.cmim, k=num_fea)), ("linear svm", svm.LinearSVC())]
    )

    results = cross_val_score(pipeline, X, y, cv=kfold)
    print(f"Accuracy: {results.mean()}")
    assert results.mean() > 0.5
