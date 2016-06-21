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
wektory = open('/home/krzysztof/Pulpit/Projekt/App/wektory','r')
z = pickle.load(wektory)
wektory.close()
x, y = z[0], z[1]
xNew = []
yNew = []

#Tasowanie danych
index_shuf = range(len(x))
shuffle(index_shuf)
for i in index_shuf:
    xNew.append(x[i])
    yNew.append(y[i])
    
Y = np.array(yNew)
X = np.array(xNew).reshape(len(xNew),len(xNew[0]))


gnb = GaussianNB()
gnb.fit(X, Y)


joblib.dump(gnb, 'model.pkl') 

print "Sukces!"
