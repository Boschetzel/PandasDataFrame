import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pickle

"""This will be the ML operations class, the GUI is ready, 
but first need to test it at script level- work in progress"""


class MlOperations:
    def __init__(self, X=None, y=None):
        pass

    # WORKFLOW FOR SCIKIT-LEARN

    # 1 Get data and clean it (remove NaN, make numeric columns ...)
    path = os.getcwd()
    df = pd.read_csv(f"{path}\\input_data\\Covid Live.csv")

    # Fill  NaN values
    df1 = df.fillna(0)

    # 2 Set training data (X) - features

    # 3 Set test data (x) - label

    # 4 Select the right model  for the problem (classification, Regression, etc)

    # 5 Fit the data to the model

    # 6 Predict data based on the model

    # 7 Evaluate the model (train data, test data) with metrics (accuracy_score, confusion_matrix...)

    # 8 Improve the model (eg. change n_estimators)

    # 9 Save the model (use pickle)

    # 10 Load the model (use pickle)
    print(df1)
