from sklearn import preprocessing, compose, model_selection
from pandas import read_csv, DataFrame, Series
from numpy import ravel, savetxt
from scipy import sparse


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

        # As movie title is now unique we can discard it
        data.drop(columns=['movie_title'], inplace=True)

        # saves imdb score as labels
        self.y = data['imdb_score']

        # Discard label from data
        data.drop(columns=['imdb_score'], axis=1, inplace=True)

        # Turn into dummy variables and discard original column from data
        genres = data.pop('genres').str.get_dummies()

    #######
        # actor1 = data['actor_1_name']
        # actor2 = data['actor_2_name']
        # actor3 = data['actor_3_name']
        # actors = actor1.str.cat(actor2, sep="|")
        # actors = actors.str.cat(actor3, sep="|")
        #
        # print(actors.head())
        # print("1",genres.head())
        #
        # actors = actors.str.get_dummies('|')
        # print("2", actors.head())
        #
        # data.drop(columns=['actor_1_name','actor_2_name','actor_3_name'], axis=1, inplace=True)
#####
        # Merge the 3 actors into one column & delete original columns from data
        # actors = data.pop('actor_1_name')+"|"+data.pop('actor_2_name')+"|"+data.pop('actor_3_name')

        # Turn into dummy variables
        # actors = actors.str.get_dummies()


        numerical_columns = data.select_dtypes(include='number').columns
        categorical_columns = data.select_dtypes(exclude='number').columns
        categorical_columns = categorical_columns.drop(["actor_1_name", "actor_2_name", "actor_3_name"])


        print("got here")
        # data["actors"] = data.join(str.cat((data.pop("actor_1_name"),data.pop["actor_2_name"]), sep="|"))
        data = data.join(data.pop('actor_1_name').str.cat(data.pop('actor_2_name'), sep="|"))
        data = data.join(data.pop('actor_1_name').str.cat(data.pop("actor_3_name"), sep="|"))
        data = data.join(data.pop("actor_1_name").str.get_dummies())
        print("and here")


        data = data.join(genres)
#         data.to_csv("features.csv")
        preprocessor = compose.ColumnTransformer(transformers=
                                                 [('num', preprocessing.StandardScaler(), numerical_columns),
                                                  ('cat', preprocessing.OneHotEncoder(), categorical_columns)],
                                                 remainder='passthrough')

        self.X = preprocessor.fit_transform(data)

        self.y = preprocessing.Binarizer(6.95).fit_transform(self.y.to_numpy().reshape(-1, 1))
        self.y = ravel(self.y)
        # savetxt('labels.csv', self.y)
    @staticmethod
    def splitToFiveFolds():
        return model_selection.KFold(n_splits=5, shuffle=False, random_state=1)

