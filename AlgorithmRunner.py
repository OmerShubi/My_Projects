from sklearn import neighbors, metrics


class AlgorithmRunner:
    def __init__(self, classifier_method, number_of_neighbors=10, p=2):
        """

        :param classifier_method:
        """
        self.algorithm = self.select_model(classifier_method, number_of_neighbors,p)
        self.accuracy = 0
        self.precision = 0
        self.recall = 0

    @staticmethod
    def select_model(classifier_method, number_of_neighbors, p):
        """

        :param classifier_method:
        :param number_of_neighbors:
        :param p:
        :return:
        """
        if classifier_method == 'KNN':
            return neighbors.KNeighborsClassifier(n_neighbors=number_of_neighbors, metric='manhattan')
        elif classifier_method == 'Rocchio':
            return neighbors.NearestCentroid()
        else:
            print("Error. Expects 'KNN' or 'Rocchio' only.")

    def fit(self, x_train, y_train):
        """

        :param x_train:
        :param y_train:
        :return:
        """
        self.algorithm.fit(x_train, y_train)

    def predict(self, x_train):
        """

        :param x_train:
        :return:
        """
        return self.algorithm.predict(x_train)

    def cross_val_score(self, data):
        """

        :param data:
        :return:
        """
        kf = data.splitToFiveFolds()
        fold = 0
        for train_index, test_index in kf.split(data.X):

            # Splits the data and labels into train and test
            x_train, x_test = data.X[train_index], data.X[test_index]
            y_train, expected = data.y[train_index], data.y[test_index]

            # Fit train data and predict test
            self.algorithm.fit(x_train, y_train)
            predicted = self.algorithm.predict(x_test)

            # Sum metrics of current iteration
            self.accuracy += metrics.accuracy_score(expected, predicted)
            self.precision += metrics.precision_score(expected, predicted, average='binary')
            self.recall += metrics.recall_score(expected, predicted, average='binary')

            fold = fold + 1
            print("Fold", fold, " out of 5 completed.")

        # Calculate average metrics
        self.accuracy = self.accuracy/fold
        self.precision = self.precision/fold
        self.recall = self.recall/fold
