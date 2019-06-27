from Data import Data
from RaceData import RaceData
from AlgorithmRunner import AlgorithmRunner


def part1(file_name):

    # Import the data from file and preprocess it
    data = Data(file_name)
    data.preprocess()

    # Initialize and run KNN classifier
    print("Running KNN Classifier...")
    classifier_knn = AlgorithmRunner('KNN')
    classifier_knn.cross_val_score(data)

    print("Running Rocchio Classifier...")
    # Initialize and run Rocchio classifier
    classifier_rocchio = AlgorithmRunner('Rocchio')
    classifier_rocchio.cross_val_score(data)

    # Display results
    print("Question 1:")
    print("KNN classifier {:.4f}, {:.4f}, {:.4f}".format(classifier_knn.precision,
                                                         classifier_knn.recall,
                                                         classifier_knn.accuracy))

    print("Rocchio classifier: {:.4f}, {:.4f}, {:.4f}".format(classifier_rocchio.precision,
                                                              classifier_rocchio.recall,
                                                              classifier_rocchio.accuracy))


def part2(file_name):
    # Import the data from file and preprocess it
    data = RaceData(file_name)
    data.preprocess()

    # Initialize and run KNN classifier
    print("Running KNN Classifier...")
    results =[]
    for k in range(3, 20, 2):

        classifier_knn = AlgorithmRunner('KNN', number_of_neighbors=k)
        classifier_knn.cross_val_score(data)
        result = classifier_knn.accuracy
        results.append(results)
        print(result)
    print(max(results), k)
    print("Running Rocchio Classifier...")
    # Initialize and run Rocchio classifier
    classifier_rocchio = AlgorithmRunner('Rocchio')
    classifier_rocchio.cross_val_score(data)

    # Display results
    print("Question 2:")
    print("KNN classifier",  classifier_knn.accuracy)
    print("Rocchio classifier:", classifier_rocchio.accuracy)


if __name__ == '__main__':

    # part1(file_name='./movie_metadata.csv')
    part2(file_name='./movie_metadata.csv')

