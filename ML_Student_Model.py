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

# https://archive.ics.uci.edu/ml/datasets/student%2Bperformance
data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]    # program bedzie wyciagal 6 danych
# oceny w trakcie pierwszego/drugiego semestru (od 0 do 20) oraz koncowa ocena
# studytime liczba godzin poswiecanona na nauke
# failures to liczba niezdanych egzaminow, max 4
# absences liczba nieobecnosci

predict = "G3"      # naszym celem jest okreslenie final grade, czyli oceny koncowej

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)    # tworzy model


best = 0    # petla do trenowania, wieksza liczba iteracji, lepsza dokladnosc modelu
'''for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)

    acc = linear.score(x_test, y_test)

    if acc > best:
        best = acc
        with open("studentmodel.pickle", "wb") as f:    # zapisy najlepszego modelu
            pickle.dump(linear, f)
            print(acc)
'''

pickle_in = open("studentmodel.pickle", "rb")   # otworzenie tegoż modelu
linear = pickle.load(pickle_in)

#acc = linear.score(x_test, y_test)
#print(acc)  # wyswietla dokladnosc modelu


predictions = linear.predict(x_test)

#for x in range(len(predictions)):
#    print(predictions[x], x_test[x], y_test[x])

p = 'G2'
style.use("ggplot")
pyplot.scatter(data[p],data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()






