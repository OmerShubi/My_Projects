from sklearn import preprocessing, compose, model_selection
from pandas import read_csv, DataFrame
from numpy import ravel


# Reads the csv file and save data to memory
class Data:
    def __init__(self, file_name):
        self.file = file_name  # path to file
        self.data = DataFrame
        self.X = DataFrame
        self.y = DataFrame

    def preprocess(self):

        # import csv
        self.data = read_csv(self.file, delimiter=',')

        # save all Attributes excluding content_Rating, movie_imdb_link, plot_keywords
        self.data.drop(columns=['content_rating', 'movie_imdb_link', 'plot_keywords'], inplace=True)

        # discard entries with any NaN value
        self.data.dropna(inplace=True)

        #  Handle duplicate movie_tile values
        self.data.drop_duplicates(subset='movie_title', keep='first', inplace=True)

        # self.data = self.data.join(self.data.pop('genres').str.get_dummies('|'))
        self.y = self.data['imdb_score']
        self.data = self.data.drop(columns=['imdb_score'], axis=1)
        numerical_columns = self.data.select_dtypes(include='number').columns
        categorical_columns = self.data.select_dtypes(exclude='number').columns

        preprocessor = compose.ColumnTransformer(transformers=
                                                 [('num', preprocessing.StandardScaler(), numerical_columns),
                                                  ('cat', preprocessing.OneHotEncoder(), categorical_columns)])

        self.X = preprocessor.fit_transform(self.data)
        self.y = preprocessing.Binarizer(7).fit_transform(self.y.to_numpy().reshape(-1, 1))
        self.y = ravel(self.y)

    @staticmethod
    def splitToFiveFolds():
        return model_selection.KFold(n_splits=5, shuffle=False, random_state=1)

