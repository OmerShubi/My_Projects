from Data import Data
from AlgorithmRunner import AlgorithmRunner


if __name__ == '__main__':

    file_name = './movie_metadata.csv'

    # Import the data from file and preprocess it
    data = Data(file_name)
    data.preprocess()

    # Initialize and run KNN classifier
    print("Running KNN Classifier...")
    classifierKNN = AlgorithmRunner('KNN')
    classifierKNN.cross_val_score(data)

    print("Running Rocchio Classifier...")
    # Initialize and run Rocchio classifier
    classifierRocchio = AlgorithmRunner('Rocchio')
    classifierRocchio.cross_val_score(data)

    print("Question 1:")
    print("KNN classifier {:.4f}, {:.4f}, {:.4f}".format(classifierKNN.precision,
                                                         classifierKNN.recall,
                                                         classifierKNN.accuracy))

    print("Rocchio classifier: {:.4f}, {:.4f}, {:.4f}".format(classifierRocchio.precision,
                                                              classifierRocchio.recall,
                                                              classifierRocchio.accuracy))

    # print("Question 2:")
    # print("KNN classifier", KNN_improved_accuracy)
    # print("Rocchio classifier:", Rocchio_improved_accuracy)
