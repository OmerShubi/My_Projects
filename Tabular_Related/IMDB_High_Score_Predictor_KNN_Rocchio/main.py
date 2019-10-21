from Data import Data
from RaceData import RaceData
from AlgorithmRunner import AlgorithmRunner
from RaceAlgorithmRunner import RaceAlgorithmRunner

import sys
import pathlib

def part1(file_name):

    print("Question 1:")

    # Import the data from file and preprocess it
    data = Data(file_name)
    data.preprocess()

    # Initialize and run KNN classifier
    # print("Running KNN Classifier...")
    classifier_knn = AlgorithmRunner('KNN')
    classifier_knn.cross_val_score(data)

    # print("Running Rocchio Classifier...")
    # Initialize and run Rocchio classifier
    classifier_rocchio = AlgorithmRunner('Rocchio')
    classifier_rocchio.cross_val_score(data)

    # Display results
    print("KNN classifier: {}, {}, {}".format(classifier_knn.precision,
                                             classifier_knn.recall,
                                             classifier_knn.accuracy))

    print("Rocchio classifier: {}, {}, {}".format(classifier_rocchio.precision,
                                                  classifier_rocchio.recall,
                                                  classifier_rocchio.accuracy))


def part2(file_name):

    print("Question 2:")

    # Import the data from file and preprocess it
    data = RaceData(file_name)
    data.preprocess()

    # Initialize and run KNN classifier
    # print("Running KNN Classifier...")
    classifier_knn = RaceAlgorithmRunner('KNN', number_of_neighbors=7)
    classifier_knn.cross_val_score(data)

    # print("Running Rocchio Classifier...")
    # Initialize and run Rocchio classifier
    classifier_rocchio = RaceAlgorithmRunner('Rocchio')
    classifier_rocchio.cross_val_score(data)

    # Display results
    print("KNN classifier:",  classifier_knn.accuracy)
    print("Rocchio classifier:", classifier_rocchio.accuracy)


if __name__ == '__main__':

    try:
        # file_path = sys.argv[1]
        file_path = "movie_metadata.csv"

    except IndexError:
        print("File path missing.")
        sys.exit(1)

    if not pathlib.Path(file_path).is_file():
        print("File -", file_path,"doesn't exist.")
        sys.exit(1)

    part1(file_name=file_path)
    print("\n")
    part2(file_name=file_path)
