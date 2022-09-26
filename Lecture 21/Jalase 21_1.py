# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:39:29 2020

@author: Reza
"""

import numpy as np 
import sklearn as sk 

### Loading Dataset (Boston huoses prices dataset)
from sklearn.datasets import load_boston 
X,T = load_boston(return_X_y=True)

### Dividing Dataset to the training and testing sets 
from sklearn.model_selection import train_test_split
X_train, X_test, T_train, T_test = train_test_split(X,T,test_size=0.3)

### Feature Scaling (Normalization) 
X_train = (X_train-np.min(X_train))/(np.max(X_train)-np.min(X_train))
X_test = (X_test-np.min(X_test))/(np.max(X_test)-np.min(X_test))

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