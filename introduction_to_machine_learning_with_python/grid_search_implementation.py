import numpy as np
from sklearn.model_selection import cross_val_score


class GridSearch:
    """
    A class to perform GridSearch CV
    ...

    # TODO 1 - Write a good doc-string for this class
    """

    def __init__(self, model, params, cv=None):
        """
        :param model: Machine learning model
        :param params: A dictionary with one item as a parameter;
                       value - param name, key - parameter space
        :param cv: If int, number of cross validation
        """
        self.model_ = model
        self.params_ = params
        self.cv_ = cv

        self.best_score_ = None
        self.best_params_ = None
        self.best_model_ = None

    def fit(self, X_train, y_train):
        """
        :param X_train: Training features from the dataset
        :param y_train: Training labels (or ground-truth) of the features
        :return: None
        """

        best_score = 0

        key_name = self.params_.keys[0]

        for param in self.params_(key_name):

            # Instantiate Model
            ml_model = self.model_(param)
            # Compute CV Scores
            cv_scores = cross_val_score(ml_model, X=X_train, y=y_train, cv=self.cv_)
            # Mean CV Score
            mean_score = np.mean(cv_scores)

            if mean_score > best_score:
                self.best_score_ = mean_score
                self.best_params_ = {
                    key_name: param
                }
                self.best_model_ = ml_model
