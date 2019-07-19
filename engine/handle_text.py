#-*- coding: utf-8 -*-
import sys
sys.path.append('/home/krzysztof/Pulpit/text2vec')
import text2vec as t
import joblib as jl


class CommentHandler:
	
	def __init__(self):
		self.model = t.TextModel()
		self.model.load('/home/krzysztof/Pulpit/Projekt/engine/model/model2')
		self.classifier = jl.load('/home/krzysztof/Pulpit/Projekt/engine/model/svmModel')

	def classify(self,comment):
		vector = [self.model.vectorize(comment.encode('utf-8').decode('utf-8'))]
		prediction = self.classifier.predict(vector)
		if prediction == 0:
			return 'obr'
		else:
			return 'dop'	

	def vector(self,comment):
		vector = [self.model.vectorize(comment.encode('utf-8').decode('utf-8'))]
		tfvec = self.tfidf.transform(vector)
		return tfvec
	
