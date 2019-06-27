from sklearn import neighbors, metrics


class RaceAlgorithmRunner:
    def __init__(self, classifier_method, number_of_neighbors):
        """
        Initializes the AlgorithRunner with the desired classifier
        :param classifier_method: desired classifier, expects 'KNN' or 'Rocchio'
        :param number_of_neighbors: the number of neighbors for knn model
        """
        self.algorithm = self.select_model(classifier_method, number_of_neighbors)
        self.accuracy = 0
        self.precision = 0
        self.recall = 0

    @staticmethod
    def select_model(classifier_method, number_of_neighbors=10):
        """
        Initializes desired classifier
        :param classifier_method: desired classifier, expects 'KNN' or 'Rocchio'
        :param number_of_neighbors: the number of neighbors for knn model, default 10
        :return: classifier sklearn object
        """
        if classifier_method == 'KNN':
            return neighbors.KNeighborsClassifier(n_neighbors=number_of_neighbors, metric='manhattan')
        elif classifier_method == 'Rocchio':
            return neighbors.NearestCentroid()
        else:
            print("Error. Expects 'KNN' or 'Rocchio' only.")

    def fit(self, x_train, y_train):
        """
        Fit the  model according to the given training data.
        :param x_train: training data
        :param y_train: training labels
        :return: the the specific algorithm fit
        """
        self.algorithm.fit(x_train, y_train)

    def predict(self, x_test):
        """
        Perform classification on an array of test vectors x_test
        :param x_test: test data
        :return: The predicted class C for each sample in x_test
        """
        return self.algorithm.predict(x_test)

    def cross_val_score(self, data):
        """
        calculates the precision, accuracy, and recall of the given model
        with the data, using 5-fold cross validation
        :param data: all data
        :return: None
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
