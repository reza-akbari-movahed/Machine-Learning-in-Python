# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:12:17 2020

@author: Reza
"""

import numpy as np 

### Loading Wine Recognition Dataset 
from sklearn.datasets import load_wine 
X,L = load_wine(return_X_y=True)

### Dividing Dataset to the training and testing sets 
from sklearn.model_selection import train_test_split
X_train, X_test, L_train, L_test = train_test_split(X,L,test_size=0.3)

### Standardization on training and testing sets 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

### Loading SVM Models
from sklearn.svm import SVC 
LIN_SVM_Model = SVC(kernel='linear')
RBF_SVM_Model = SVC(kernel='rbf')
POL_SVM_Model = SVC(kernel='poly',degree=2)

### Training the Models 
LIN_SVM_Model.fit(X_train,L_train)
RBF_SVM_Model.fit(X_train,L_train)
POL_SVM_Model.fit(X_train,L_train)

### Predicting the testing samples 
Pre_LIN_SVM = LIN_SVM_Model.predict(X_test)
Pre_RBF_SVM = RBF_SVM_Model.predict(X_test)
Pre_POL_SVM = POL_SVM_Model.predict(X_test)

### Evaluating the trained models 
SC_LIN_SVM = LIN_SVM_Model.score(X_test,L_test)
SC_RBF_SVM = RBF_SVM_Model.score(X_test,L_test)
SC_POL_SVM = POL_SVM_Model.score(X_test,L_test)
