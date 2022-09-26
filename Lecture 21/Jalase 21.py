# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:09:35 2020

@author: Reza
"""

import numpy as np 
import sklearn as sk 

### Loading Diabet Dataset 
from sklearn.datasets import load_diabetes
X,T = load_diabetes(return_X_y=True)

### Dividing Dataset to the training and testing sets 
from sklearn.model_selection import train_test_split
X_train, X_test, T_train, T_test = train_test_split(X,T,test_size=0.3)

### Standardization on training and testing sets 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


### Loading an SVM Regression model 
from sklearn.svm import SVR 
Model = SVR()

### Training the Regression model 
Model.fit(X_train,T_train)

### Testing the trained regression model 
Estimated_Target_Tests = Model.predict(X_test)

### Evaluating the regression model 
from sklearn.metrics import mean_squared_error 
MSE_Test = mean_squared_error(T_test,Estimated_Target_Tests)
