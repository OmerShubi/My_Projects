import sklearn

class AlgorithmRunner:
    def __init__(self, classifier_method):
        self.algorithm = classifier_method
        self.model = self.selectModel()

    def selectModel(self):
        if self.algorithm == 'KNN':
            return sklearn.neighbors.KNeighborsClassifier(n_neighbors=10)
        elif self.algorithm == 'Rocchio':
            return sklearn.neighbors.NearestCentroid()
        else:
            print("Error. Expects 'KNN' or 'Rocchio' only.")

    def fit(self, X_train, y_train):
        self.model.fit( X_train, y_train)

    def predict(self, X_test):
        self.model.predict(X_test)
