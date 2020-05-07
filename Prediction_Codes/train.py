import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from joblib import dump
from preprocess import prep_data
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error

df = pd.read_csv(("fish_participant.csv"))

X, y = prep_data(df)

kf = KFold(n_splits = 20, shuffle = True, random_state = 55)
kf.get_n_splits(X)

print(kf)

for train_index, test_index in kf.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    

wrf = RandomForestClassifier(class_weight = "balanced")
wrf.fit(X_train, y_train)
y_pred = wrf.predict(X_test)
print(mean_squared_error(y_test,y_pred))

# nb = GaussianNB()
# nb.fit(X, y)

# lr = LinearRegression()
# lr.fit(X,y)

dump(wrf, "wrf.joblib")