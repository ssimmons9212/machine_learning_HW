### YOU WRITE THIS ###
import os
from joblib import load
from preprocess import prep_data
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from preprocess import prep_data
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report

def predict_from_csv(path_to_csv):

    df = pd.read_csv(path_to_csv)
    X, y = prep_data(df)

    reg = load("wrf.joblib")
    # reg = load("gnb.joblib")
    # reg = load("lr.joblib")


    predictions = reg.predict(X)

    return predictions

if __name__ == "__main__":
    predictions = predict_from_csv(("fish_holdout_demo.csv"))
    print(predictions)
    print(pd.read_csv("fish_holdout_demo.csv")["Weight"].values)
######

### WE WRITE THIS ###
    # from sklearn.metrics import mean_squared_error
    # from sklearn.metrics import classification_report
    # ho_predictions = predict_from_csv("fish_holdout.csv")
    # ho_truth = pd.read_csv("fish_holdout.csv")["Weight"].values
    # ho_mse = mean_squared_error(ho_truth, ho_predictions)
    # print(ho_mse)
######

