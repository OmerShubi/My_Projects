from sklearn.datasets import load_digits
import pandas as pd
import Data
import AlgorithmRunner
import sklearn

import AlgorithmRunner


if __name__ == '__main__':
    file_name = './movie_metadata.csv'

    data = Data.Data(file_name)
    data = data.preprocess()
    X_train, X_test, y_train, y_test = data.splitToFiveFolds()
    classifier = AlgorithmRunner('KNN')
    classifier.fit(X_train, y_train)
    classifier.predict(X_test)
    # TODO KNN (K=10) 5-fold Cross Validation
    # TODO Rocchio 5-fold Cross Validation
    # TODO for each - Precision, Recall, Accuracy

    print("Question 1:")
    # print("KNN classifier", KNN_precision, KNN_recall, KNN_accuracy)
    # print("Rocchio classifier:", Rocchio_precision, Rocchio_recall, Rocchio_accuracy)

    print("Question 2:")
    # print("KNN classifier", KNN_improved_accuracy)
    # print("Rocchio classifier:", Rocchio_improved_accuracy)


