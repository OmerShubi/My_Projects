from sklearn import preprocessing, compose, model_selection
import pandas as pd
from numpy import ravel
GOODMOVIETHRESHOLD = 6.95
NUMBEROFFOLDS = 5


# Reads the csv file and save data to memory
class Data:
    def __init__(self, file_name):
        """
        Initializes the class
        :param file_name: path to file
        """
        self.file = file_name  # path to file
        self.X = pd.DataFrame  # Data without Labels
        self.y = pd.DataFrame  # Labels

    def preprocess(self):
        """
        Preprocesses the data according to specified demands and for the classifiers
        :return: None
        """
        # Display current operation
        print("Reading csv, dropping excluded columns, movie duplicates and rows with na values...")

        # import csv
        data = pd.read_csv(self.file, delimiter=',')

        # save all Attributes excluding content_Rating, movie_imdb_link, plot_keywords
        data.drop(columns=['content_rating', 'movie_imdb_link', 'plot_keywords'], inplace=True)

        # discard entries with any NaN value
        data.dropna(inplace=True)

        #  Handle duplicate movie_tile values
        data.drop_duplicates(subset='movie_title', keep='first', inplace=True)

        # As movie title is now unique we can discard it
        data.drop(columns=['movie_title'], inplace=True)

        # saves imdb score as labels & Discard label from data
        self.y = data.pop('imdb_score')

        # Display current operation
        print("Turning genres column and the 3 actors to dummy variables...")

        # Turn into dummy variables and discard original column from data
        genres = data.pop('genres').str.get_dummies()

        # Merge the 3 actors into one column & delete original columns from data & Turn into dummy variables
        actors = (data.pop('actor_1_name')+"|"+data.pop('actor_2_name')+"|"+data.pop('actor_3_name')).str.get_dummies()

        # Create column lists for transformer
        numerical_cols = data.select_dtypes(include='number').columns
        categorical_cols = data.select_dtypes(exclude='number').columns

        # After creating the column lists - joins back the dummy-variable actors and genres
        data = data.join(actors)
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
        Initializes the sklearn KFold object with NUMBEROFFOLDS(5) for slicing the data
        :return: model_selection.KFold
        """
        return model_selection.KFold(n_splits=NUMBEROFFOLDS, shuffle=False, random_state=1)
