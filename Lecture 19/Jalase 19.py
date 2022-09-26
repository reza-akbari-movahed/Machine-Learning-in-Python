# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:05:25 2020

@author: Reza
"""

import pandas as pd 
import numpy as np 

Link = "E:\\My Cources\\Machine Learning With Python\\991\Jalase 19\\heart.csv"

Data = pd.read_csv(Link)
Data_arr = pd.DataFrame.to_numpy(Data)
L = Data_arr[:,13]
X = Data_arr[:,0:13]

from sklearn.model_selection import KFold
from sklearn.naive_bayes import GaussianNB 
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
Model = GaussianNB()

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

 
