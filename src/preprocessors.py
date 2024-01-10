"""Preprocessor"""

import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder


class CategoricalImputer(BaseEstimator, TransformerMixin):
    """Categorical missing value imputer"""

    def __init__(self, variables=None):
        """__init__"""

        self.variables = variables

    def fit(self, X, y=None):
        """fit"""

        # we need the fit statement to accomodate the sklearn pipeline
        return self

    def transform(self, X):
        """transform"""

        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna("Missing")

        return X


class NumericalImputer(BaseEstimator, TransformerMixin):
    """Numerical missing value imputer"""

    def __init__(self, variables=None):
        """__init__"""

        self.variables = []

    def fit(self, X, y=None):
        """fit"""

        self.variables = [var for var in X.columns if X[var].dtype != "O"]

        # persist mode in a dictionary
        self.imputer_dict_ = {}

        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].mode()[0]
        return self

    def transform(self, X):
        """transform"""

        X = X.copy()
        for feature in self.variables:
            X[feature].fillna(self.imputer_dict_[feature], inplace=True)
        return X


class TemporalVariableEstimator(BaseEstimator, TransformerMixin):
    """Temporal variable calculator"""

    def __init__(self, variables=None, reference_variable=None):
        """__init__"""

        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

        self.reference_variables = reference_variable

    def fit(self, X, y=None):
        """fit"""

        # we need this step to fit the sklearn pipeline
        return self

    def transform(self, X):
        """transform"""

        X = X.copy()
        for feature in self.variables:
            X[feature] = X[self.reference_variables] - X[feature]

        return X


class CategoricalToNumerical(BaseEstimator, TransformerMixin):
    """Transform categorical to numerical"""

    def __init__(self, variables=None):
        """__init__"""

        self.variables = variables

    def fit(self, X, y=None):
        """fit"""

        return self

    def transform(self, X):
        """transform"""

        def object_to_num(x):
            """cast object to num"""

            if x is not np.nan:
                x = "".join(x.split(","))

            return x

        for feature in self.variables:

            X[feature] = X[feature].apply(object_to_num)
            X[feature] = X[feature].astype(float)
        return X


class RareLabelCategoricalEncoder(BaseEstimator, TransformerMixin):
    """Frequent label categorical encoder"""

    def __init__(self, tol=0.05, variables=None):
        """__init__"""

        self.tol = tol

        self.variables = variables

    def fit(self, X, y=None):
        """fit"""

        # persist frequent labels in dictionary
        self.encoder_dict_ = {}

        for var in self.variables:
            # the encoder will learn the most frequent categories
            t = pd.Series(X[var].value_counts() / float(len(X)))
            # frequent labels:
            self.encoder_dict_[var] = list(t[t >= self.tol].index)

        return self

    def transform(self, X):
        """transform"""

        X = X.copy()
        for feature in self.variables:
            X[feature] = np.where(
                X[feature].isin(self.encoder_dict_[feature]), X[feature], "Rare"
            )

        return X


class CategoricalEncoder(BaseEstimator, TransformerMixin):
    """String to numbers categorical encoder"""

    def __init__(self, variables=None, target=None):
        """__init__"""

        self.variables = variables

    def fit(self, X, y=None):
        """fit"""

        self.enc = OneHotEncoder(handle_unknown="ignore")
        # persist transforming dictionary

        if len(self.variables) == 1:
            self.enc.fit(np.array(X[self.variables[0]]).reshape(-1, 1))

        else:
            self.enc.fit(np.array(X[self.variables]))

        return self

    def transform(self, X):
        """transform"""

        # encode labels
        X = X.copy()

        if len(self.variables) == 1:
            X_enc = self.enc.transform(
                np.array(X[self.variables[0]]).reshape(-1, 1)
            ).toarray()

        else:
            X_enc = self.enc.transform(np.array(X[self.variables])).toarray()

        X_enc = pd.DataFrame(
            X_enc,
            columns=[
                self.variables[j] + "_" + str(i)
                for j in range(len(self.variables))
                for i in range(len(self.enc.categories_[j]))
            ],
        )

        X = pd.concat([X, X_enc], axis=1).drop(self.variables, axis=1)

        return X


class LogTransformer(BaseEstimator, TransformerMixin):
    """Logarithm transformer"""

    def __init__(self, variables=None):
        """__init__"""

        self.variables = []

    def fit(self, X, y=None):
        """fit"""

        # to accomodate the pipeline
        self.variables = [var for var in X.columns if X[var].dtype != "O"]

        return self

    def transform(self, X):
        """transform"""

        X = X.copy()

        for feature in self.variables:
            X[feature] = np.log(X[feature])

        return X


class DropUnecessaryFeatures(BaseEstimator, TransformerMixin):
    """Drop unecessary features"""

    def __init__(self, variables_to_drop=None):
        """__init__"""

        self.variables = variables_to_drop

    def fit(self, X, y=None):
        """fit"""

        return self

    def transform(self, X):
        """transform"""

        # encode labels
        X = X.copy()
        X = X.drop(self.variables, axis=1)

        return X


class LabelExtraction(BaseEstimator, TransformerMixin):
    """Label Extraction"""

    def __init__(self, variables=None):
        """__init__"""

        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        """fit"""

        return self

    def transform(self, X):
        """transform"""

        X = X.copy()

        for feature in self.variables:
            for i in range(X.shape[0]):
                try:
                    X[feature][i] = X[feature][i].split(",")[0]
                except Exception:
                    pass

        return X
