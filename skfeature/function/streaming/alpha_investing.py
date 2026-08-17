import numpy as np
from sklearn import linear_model
from sklearn.base import BaseEstimator, TransformerMixin


def alpha_investing(X, y, w0, dw):
    """
    This function implements streamwise feature selection (SFS) algorithm alpha_investing for binary regression or
    univariate regression

    Input
    -----
    X: {numpy array}, shape (n_samples, n_features)
        input data, assume feature arrives one at each time step
    y: {numpy array}, shape (n_samples,)
        input class labels or regression target

    Output
    ------
    F: {numpy array}, shape (n_selected_features,)
        index of selected features in a streamwise way

    Reference
    ---------
    Zhou, Jing et al. "Streaming Feature Selection using Alpha-investing." KDD 2006.
    """

    n_samples, n_features = X.shape
    w = w0
    F = []  # selected features
    for i in range(n_features):
        x_can = X[:, i]  # generate next feature
        alpha = w / 2 / (i + 1)
        # when no features have been selected yet, compare against the intercept-only model
        X_old = np.ones((n_samples, 1)) if not F else X[:, F]
        linreg_old = linear_model.LinearRegression()
        linreg_old.fit(X_old, y)
        error_old = 1 - linreg_old.score(X_old, y)

        # model built with X_old & {x_can}
        X_new = np.concatenate((X_old, x_can.reshape(n_samples, 1)), axis=1)
        logreg_new = linear_model.LinearRegression()
        logreg_new.fit(X_new, y)
        error_new = 1 - logreg_new.score(X_new, y)

        # calculate p-value
        pval = np.exp((error_new - error_old) / (2 * error_old / n_samples))
        if pval < alpha:
            F.append(i)
            w = w + dw - alpha
        else:
            w -= alpha
    return np.array(F)


class AlphaInvesting(BaseEstimator, TransformerMixin):
    """
    Implmenetation of alpha-investing that is compatible with sklearn pipelines.

    Reference
    ---------
    Zhou, Jing et al. "Streaming Feature Selection using Alpha-investing." KDD 2006.
    """

    def __init__(self, w0, dw):
        self.w0 = w0
        self.dw = dw
        self.F = []  # selected features

    def fit(self, X, y=None):
        if y is None:
            raise ValueError("alpha-investing requires target values y")
        self.F = alpha_investing(X[:], y[:], self.w0, self.dw)
        return self

    def transform(self, X):
        return X[:, self.F]
