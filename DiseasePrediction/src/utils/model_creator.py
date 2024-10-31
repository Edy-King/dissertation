import os
import joblib
import pandas as pd
import xgboost as xgb
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

"""
This class is used to create models.
It has methods to create each model implementation. 
creating that model is just a case of instantiating the class and calling the function to create the model.
The pre_process_data method is an internal/private method that should be called by the methods of the class to get the 
preprocessed data. 
It can also be called on its own to work with the X and Y train dataframes.
"""

class ModelCreator:
    def __init__(self, data_path):
        self.df = None
        self.data_path = data_path


    # ################################################
    # ### load data method
    # #################################################
    def load_data(self):
        print("Loading data...")
        try:
            self.df = pd.read_csv(self.data_path)
        except FileNotFoundError:
            print(f"Error: The file '{self.data_path}' was not found.")
            print(f"Current working directory: {os.getcwd()}")
            print("Please ensure the file exists and the path is correct.")
            raise
        except Exception as e:
            print(f"An error occurred while loading the data: {str(e)}")
            raise

    # ################################################
    # ### pre-process data
    # #################################################
    def pre_process_data(self):
        if self.df is None:
            self.load_data()

        ### get columns to be kept
        columns_to_keep = ['cough', 'fever', 'sore_throat', 'shortness_of_breath', 'head_ache', 'corona_result']
        ### create a new dataframe keeping only the correct columns
        df = self.df[columns_to_keep]

        ### Reassign integers(0 & 1) in place of Negative and Positive strings in the corona_result column
        df['corona_result'] = df['corona_result'].map({'Negative': 0, 'Positive': 1})

        ### split the dataframe to target and independent vars
        Y = df['corona_result']
        X = df.drop(['corona_result'], axis=1)

        ### implement under-sampling and over sampling
        undersample = RandomUnderSampler(sampling_strategy={0: 500000, 1: 500000}, random_state=33)
        X_under, Y_under = undersample.fit_resample(X, Y)

        ### split into test and train sets
        X_train, X_test, Y_train, Y_test = train_test_split(X_under, Y_under, test_size=0.2, random_state=42)

        return X_train, X_test, Y_train, Y_test

    # ################################################
    # ### create random forest model
    # #################################################
    def create_random_forest(self):
        ### get preprocessed data
        X_train, X_test, Y_train, Y_test = self.pre_process_data()

        ###  Initialize the random forest classifier
        print('Creating random forest model...')
        rfc = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)

        ### fit the data
        rfc.fit(X_train, Y_train)

        # Create the 'model' directory if it doesn't exist
        os.makedirs('./models', exist_ok=True)

        # Save the model
        joblib.dump(rfc, './models/random_forest_model.joblib')

        print('Random forest model created.')
        return True

    # ################################################
    # ### create xgboost model
    # #################################################
    def create_xgboost(self):
        ### get preprocessed data
        X_train, X_test, Y_train, Y_test = self.pre_process_data()

        ###  Initialize the xgboost model
        print('Creating xgboost model...')
        dtrain = xgb.DMatrix(X_train, label=Y_train)

        ### fit the data
        params = {
            'max_depth': 3,
            'eta': 0.1,
            'objective': 'multi:softmax',
            'num_class': 3}

        # Training the Model
        model = xgb.train(params, dtrain, num_boost_round=10)

        # Create the 'model' directory if it doesn't exist
        os.makedirs('./models', exist_ok=True)

        # Save the model
        joblib.dump(model, './models/xgboost_model.joblib')

        print('XGBoost model created.')
        return True

    # ################################################
    # ### create logistic regression model
    # #################################################
    def create_logistic_regression(self):
        ### get preprocessed data
        X_train, X_test, Y_train, Y_test = self.pre_process_data()

        ### Initialize the logistic regression classifier
        print('Creating logistic regression model...')
        log_reg = LogisticRegression(max_iter=1000, random_state=42)

        ### fit the data
        log_reg.fit(X_train, Y_train)

        # Create the 'model' directory if it doesn't exist
        os.makedirs('./models', exist_ok=True)

        # Save the model
        joblib.dump(log_reg, './models/logistic_regression_model.joblib')

        print('Logistic regression model created.')
        return True

    # ################################################
    # ### create naive bayes model
    # #################################################
    def create_naive_bayes(self):
        ### get preprocessed data
        X_train, X_test, Y_train, Y_test = self.pre_process_data()

        ### Initialize the naive bayes classifier
        print('Creating naive bayes model...')
        nb_model = GaussianNB()

        ### fit the data
        nb_model.fit(X_train, Y_train)

        # Create the 'model' directory if it doesn't exist
        os.makedirs('./models', exist_ok=True)

        # Save the model
        joblib.dump(nb_model, './models/naive_bayes_model.joblib')

        print('Naive bayes model created.')
        return True

    # ################################################
    # ### Create KNN
    # #################################################
    def create_knn(self):
            ### get preprocessed data
        X_train, X_test, Y_train, Y_test = self.pre_process_data()

        ### Initialize KNN classifier
        print('Creating knn_model...')
        knn_model = GaussianNB()

        ### fit the data
        knn_model.fit(X_train, Y_train)

        # Create the 'model' directory if it doesn't exist
        os.makedirs('./models', exist_ok=True)

        # Save the model
        joblib.dump(knn_model, './models/knn_model.joblib')

        print('knn model created.')
        return True

    # ################################################
    # ### Svm model
    # #################################################
    def create_svm(self):
        ### get the test and train data
        X_train, X_test, Y_train, Y_test = self.pre_process_data()

        pca = PCA(n_components=2) # reduce the dimensions to 2 for visualization
        X_train_pca = pca.fit_transform(X_train)
        X_test_pca = pca.transform(X_test)

        svm_model = SVC(kernel='linear') # use a linear kernel for simplicity

        # Train the classifier on the PCA-transformed training data
        print('fitting the model')
        svm_model.fit(X_train_pca, Y_train)

        # Create the 'model' directory if it doesn't exist
        os.makedirs('./models', exist_ok=True)

        # Save the model
        print('saving the model')
        joblib.dump(svm_model, './models/svm_pca.joblib')

        return True


