#-*- coding: utf-8 -*-
import sys
sys.path.append('/home/krzysztof/Pulpit/text2vec')
import text2vec as t
#from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import TfidfTransformer as tfidf
#~ from keras.layers.core import Dense, Activation
#~ from keras.models import Sequential
#~ from keras.optimizers import RMSprop
#~ from keras.utils import np_utils
from sklearn import svm
from sklearn.externals import joblib
import numpy as np
import joblib as jl


class CommentHandler:
	
	def __init__(self):
		#Wektoryzacja
		#self.model = c.load('/home/krzysztof/Pulpit/Projekt/text2vec/oznaczone')
		self.model = t.TextModel()
		self.model.load('/home/krzysztof/Pulpit/Projekt/Silnik/model/model2')
		#self.tfidf = joblib.load('/home/krzysztof/Pulpit/Projekt/Silnik/tfidf_model')
		#Ładowanie 
		#self.classifier = joblib.load('/home/krzysztof/Pulpit/Projekt/Silnik/model/model2') 
		#Klasyfikator
		#~ self.neuro = Sequential()
		#~ self.neuro.add(Dense(1024, input_shape=(inp2,)))
		#~ self.neuro.add(Activation('relu'))
		#~ self.neuro.add(Dense(512))
		#~ self.neuro.add(Activation('relu'))
		#~ self.neuro.add(Dense(2))
		#~ self.neuro.add(Activation('softmax'))		
		self.classifier = jl.load('/home/krzysztof/Pulpit/Projekt/Silnik/model/svmModel')
		#~ rms = RMSprop()
		#~ self.neuro.compile(loss='categorical_crossentropy', optimizer=rms)
		#~ self.neuro.load_weights('/home/krzysztof/Pulpit/Projekt/Silnik/neuro_model')
	
	def classify(self,comment):
		vector = [self.model.vectorize(comment.encode('utf-8').decode('utf-8'))]
		#vector = self.vector(comment)
		#print len(vector)
		prediction = self.classifier.predict(vector)
		if prediction == 0:
			return 'obr'
		else:
			return 'dop'	
		#return 'obr'	

	def vector(self,comment):
		vector = [self.model.vectorize(comment.encode('utf-8').decode('utf-8'))]
		tfvec = self.tfidf.transform(vector)
		return tfvec
	
