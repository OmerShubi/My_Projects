from sklearn import preprocessing, compose, model_selection
from pandas import read_csv, DataFrame, Series
from numpy import ravel, savetxt, concatenate
from scipy import sparse


# Reads the csv file and save data to memory
class Data:
    def __init__(self, file_name):
        self.file = file_name #  path to file
        self.X = DataFrame  # Data without Labels
        self.y = DataFrame  # Labels

    def preprocess(self):

        # import csv
        data = read_csv(self.file, delimiter=',')

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

        # Turn into dummy variables and discard original column from data
        genres = data.pop('genres').str.get_dummies()
        # Merge the 3 actors into one column & delete original columns from data & Turn into dummy variables
        actors = (data.pop('actor_1_name')+"|"+data.pop('actor_2_name')+"|"+data.pop('actor_3_name')).str.get_dummies()

        # Create column lists for transformer
        numerical_columns = data.select_dtypes(include='number').columns
        categorical_columns = data.select_dtypes(exclude='number').columns

        data = data.join(genres)
        data = data.join(actors)

        preprocessor = compose.ColumnTransformer(transformers=
                                                 [('num', preprocessing.StandardScaler(), numerical_columns),
                                                  ('cat', preprocessing.OneHotEncoder(), categorical_columns)],
                                                 remainder="passthrough")

        self.X = preprocessor.fit_transform(data)
        # actors = actors.to_sparse()
        # genres = genres.to_sparse()
        # sel.X
        self.y = preprocessing.Binarizer(6.95).fit_transform(self.y.to_numpy().reshape(-1, 1))
        self.y = ravel(self.y)

    @staticmethod
    def splitToFiveFolds():
        return model_selection.KFold(n_splits=5, shuffle=False, random_state=1)

