import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from joblib import dump
from preprocess import prep_data

df = pd.read_csv(("fish_participant.csv"))

X, y = prep_data(df)

wrf = RandomForestClassifier(class_weight = "balanced")
wrf.fit(X, y)

# nb = GaussianNB()
# nb.fit(X, y)

# lr = LinearRegression()
# lr.fit(X,y)

dump(wrf, "wrf.joblib")