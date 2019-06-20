import sklearn

class AlgorithmRunner:
    def __init__(self, classifier_method):
        self.algorithm = self.select_model(classifier_method)

    @staticmethod
    def select_model(classifier_method):
        if classifier_method == 'KNN':
            return sklearn.neighbors.KNeighborsClassifier(n_neighbors=10)
        elif classifier_method == 'Rocchio':
            return sklearn.neighbors.NearestCentroid()
        else:
            print("Error. Expects 'KNN' or 'Rocchio' only.")

    def fit(self, X_train, y_train):
        self.algorithm.fit( X_train, y_train)

    def predict(self, X_test):
        self.algorithm.predict(X_test)
