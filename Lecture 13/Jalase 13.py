# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:57:49 2020

@author: Reza
"""


import numpy as np
import sklearn as sk 

#### Loading Iris Dataset 
from sklearn.datasets import load_iris
X,L = load_iris(return_X_y=True) 

### Dividing Dataset to the training and testing sets 
from sklearn.model_selection import train_test_split
X_train, X_test, L_train, L_test = train_test_split(X,L,test_size=0.3)

### Loading LDA Classifier 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
Model = LinearDiscriminantAnalysis()

### Standardization on training and testing sets 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

### Normalization on training and testing sets
#X_train = (X_train-np.min(X_train))/(np.max(X_train)-np.min(X_train)) 
#X_test = (X_test-np.min(X_test))/(np.max(X_test)-np.min(X_test)) 


### Training the classifier model 
Model.fit(X_train,L_train)

### Predicting the testing samples
Predict = Model.predict(X_test)
