from sklearn import svm
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline

from skfeature.function.statistical_based import chi_square
from skfeature.utility.util import loadmat


def test_chi2():
    mat = loadmat("./data/BASEHOCK.mat")
    X = mat["X"]  # data
    X = X.astype(float)
    y = mat["Y"]  # label
    y = y[:, 0]

    num_fea = 100  # number of selected features
    kfold = KFold(n_splits=2, shuffle=True)

    # build pipeline
    pipeline = Pipeline(
        [("select top k", SelectKBest(score_func=chi_square.chi_square, k=num_fea)), ("linear svm", svm.LinearSVC())]
    )

    results = cross_val_score(pipeline, X, y, cv=kfold)
    print(f"Accuracy: {results.mean()}")
    assert results.mean() > 0.5
