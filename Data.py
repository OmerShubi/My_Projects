from sklearn import preprocessing, compose, model_selection
from pandas import read_csv, DataFrame
from numpy import ravel


# Reads the csv file and save data to memory
class Data:
    def __init__(self, file_name):
        self.file = file_name  # path to file
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

        # data = data.join(data.pop('genres').str.get_dummies('|'))
        self.y = data['imdb_score']
        data = data.drop(columns=['imdb_score'], axis=1)
        numerical_columns = data.select_dtypes(include='number').columns
        categorical_columns = data.select_dtypes(exclude='number').columns

        preprocessor = compose.ColumnTransformer(transformers=
                                                 [('num', preprocessing.StandardScaler(), numerical_columns),
                                                  ('cat', preprocessing.OneHotEncoder(), categorical_columns)],
                                                 remainder='passthrough')

        self.X = preprocessor.fit_transform(data)
        self.y = preprocessing.Binarizer(7).fit_transform(self.y.to_numpy().reshape(-1, 1))
        self.y = ravel(self.y)

    @staticmethod
    def splitToFiveFolds():
        return model_selection.KFold(n_splits=5, shuffle=False, random_state=1)

