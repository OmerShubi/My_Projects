from sklearn import preprocessing, compose, model_selection
import pandas as pd
from numpy import ravel
GOODMOVIETHRESHOLD = 6.95
NUMBEROFFOLDS = 5


# Reads the csv file and save data to memory
class RaceData:
    def __init__(self, file_name):
        """

        :param file_name:
        """
        self.file = file_name  # path to file
        self.X = pd.DataFrame  # Data without Labels
        self.y = pd.DataFrame  # Labels

    def preprocess(self):
        """

        :return:
        """
        # Display current operation
        print("Reading csv, dropping excluded columns, movie duplicates and rows with na values...")

        # import csv
        data = pd.read_csv(self.file, delimiter=',', usecols=['movie_title',
                                                              'imdb_score',
                                                              'num_voted_users',
                                                              'budget',
                                                              'genres'])

        # discard entries with any NaN value
        data.dropna(inplace=True)

        #  Handle duplicate movie_tile values
        data.drop_duplicates(subset='movie_title', keep='first', inplace=True)

        # As movie title is now unique we can discard it
        data.drop(columns=['movie_title'], inplace=True)

        # saves imdb score as labels & Discard label from data
        self.y = data.pop('imdb_score')

        # Display current operation
        print("Turning genres column to dummy variables...")

        # Turn into dummy variables and discard original column from data
        genres = data.pop('genres').str.get_dummies()

        # Create column lists for transformer
        numerical_cols = data.select_dtypes(include='number').columns
        categorical_cols = data.select_dtypes(exclude='number').columns

        # After creating the column lists - joins back the dummy-variable  genres
        data = data.join(genres)

        # Display current operation
        print("Applying Standard Scaler to numerical columns and OneHotEncoder for remaining categorical columns...")

        preprocessor = compose.ColumnTransformer(transformers=[('num', preprocessing.StandardScaler(), numerical_cols),
                                                 ('cat', preprocessing.OneHotEncoder(), categorical_cols)],
                                                 remainder="passthrough")

        self.X = preprocessor.fit_transform(data)

        # Display current operation
        print("Binarizing Labels...")

        # all labels lower that 7 become 0, 7 and higher become 1
        self.y = preprocessing.Binarizer(GOODMOVIETHRESHOLD).fit_transform(self.y.to_numpy().reshape(-1, 1))
        self.y = ravel(self.y)

        # Display current operation
        print("Data preprocessing complete.")

    @staticmethod
    def splitToFiveFolds():
        """

        :return:
        """
        return model_selection.KFold(n_splits=NUMBEROFFOLDS, shuffle=False, random_state=1)
