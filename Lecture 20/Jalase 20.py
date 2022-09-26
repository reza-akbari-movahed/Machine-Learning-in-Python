# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:36:23 2020

@author: Reza
"""

import numpy as np 
from sklearn.datasets import load_wine 
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn import tree 

X,L = load_wine(return_X_y=True)

sc = StandardScaler()
Model = tree.DecisionTreeClassifier()

kf = KFold(n_splits=10)
kf.get_n_splits(X,L)

ACC_Whole = [] 

for train_index, test_index in kf.split(X,L):
    X_train = X[train_index,:]
    L_train = L[train_index]
    X_test = X[test_index,:]
    L_test = L[test_index]
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    Model.fit(X_train,L_train)
    ACC = Model.score(X_test,L_test)
    ACC_Whole.append(ACC)
    
ACC_Whole = np.asarray(ACC_Whole)
Mean_ACC = np.mean(ACC_Whole)
