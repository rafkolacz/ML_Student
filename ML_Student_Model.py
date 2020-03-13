import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import  shuffle
import keras
import tensorflow
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
import math

# https://archive.ics.uci.edu/ml/datasets/student%2Bperformance
print("Reading data...\n")
data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]    # abstract 6 parameters


predict = "G3"      # program will predict final grade

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

# print("Creating model...\n")

# x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)    # create model

best = 0    # loop for training, for better performance use colab
'''for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)

    acc = linear.score(x_test, y_test)

    if acc > best:
        best = acc
        with open("studentmodel.pickle", "wb") as f:    # save the best model
            pickle.dump(linear, f)
            print(acc)
'''

pickle_in = open("studentmodel.pickle", "rb")   # instead of creating model all the time
linear = pickle.load(pickle_in)                 # program will open best previous model

# acc = linear.score(x_test, y_test)
# print(acc)  # wyswietla dokladnosc modelu

# Here we can compare predicted G3 with real values K
# predictions = linear.predict(x_test)
# for x in range(len(predictions)):
#    print(predictions[x], x_test[x], y_test[x])

''' 
# for plots
p = 'studytime'
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()
'''


def calculator(x):
    research_mat = [[1, 1, 1, 1, 1]]
    if x[2] < 2:
        x[2] = 1
    elif x[2] > 1 and x[2] < 6:
        x[2] = 2
    elif x[2] > 5 and x[2] < 11:
        x[2] = 3
    elif x[2] > 10:
        x[2] = 4
    research_mat.append(x)
    predictions = linear.predict(research_mat)
    result = predictions[1]
    result = math.floor(result)
    if result < 0:
        result = 0
    if result > 20:
        result = 20
    return result





