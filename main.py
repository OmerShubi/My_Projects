from sklearn.datasets import load_digits
import pandas as pd
import Data
import sklearn

import AlgorithmRunner


if __name__ == '__main__':
    file_name = './movie_metadata.csv'

    data = Data.Data(file_name)
    data = data.preprocess()
    # TODO KNN (K=10) 5-fold Cross Validation
    # sklearn.neighbors.KNeighborsClassifier
    # TODO Rocchio 5-fold Cross Validation
    # sklearn.neighbors.NearestCentroid
    # TODO for each - Precision, Recall, Accuracy

    print("Question 1:")
    # print("KNN classifier", KNN_precision, KNN_recall, KNN_accuracy)
    # print("Rocchio classifier:", Rocchio_precision, Rocchio_recall, Rocchio_accuracy)

    print("Question 2:")
    # print("KNN classifier", KNN_improved_accuracy)
    # print("Rocchio classifier:", Rocchio_improved_accuracy)


