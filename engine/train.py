#-*- coding: utf-8 -*-

from sklearn.externals import joblib
import sys
import numpy as np
sys.path.append('/home/krzysztof/Pulpit/Projekt/text2vec')
import cPickle as pickle
from random import shuffle
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import KFold

#Deserializacja danych
vectors = open('/home/krzysztof/Pulpit/Projekt/App/wektory', 'r')
z = pickle.load(vectors)
vectors.close()
x, y = z[0], z[1]
x_new = []
y_new = []

#Tasowanie danych
index_shuf = range(len(x))
shuffle(index_shuf)
for i in index_shuf:
    x_new.append(x[i])
    y_new.append(y[i])
    
Y = np.array(y_new)
X = np.array(x_new).reshape(len(x_new), len(x_new[0]))

gnb = GaussianNB()
gnb.fit(X, Y)

joblib.dump(gnb, 'model.pkl') 

print("Sukces!")
