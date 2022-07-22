import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def prediction(marks):
    X = pd.read_csv("/home/user54/project1/train_x2.csv", encoding='utf-8')
    y = pd.read_csv("/home/user54/project1/train_y2.csv", encoding='utf-8')
    # data = data.dropna()

    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    #X = data["x"]
    #y = data["y"]

    X =X.values
    y =y.values

    model= LinearRegression()

    X = X.reshape(-1, 1)
    y = y.reshape(-1, 1)

    model.fit(X,y)

    
    X_test = np.array(marks)
    X_test = X_test.reshape((1, -1))

    return model.predict(X_test)[0]
