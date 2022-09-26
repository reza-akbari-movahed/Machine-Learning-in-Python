# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:44:48 2020

@author: Reza
"""

import numpy as np 
import pandas as pd 

Link = "E:\\My Cources\\Machine Learning With Python\\991\\Jalase 18\\breast-cancer-wisconsin-data\\data.csv"

Data = pd.read_csv(Link)

L = Data.iloc[:,1]
L = list(L)
L = np.asarray(L)

X = Data.iloc[:,2:32]
X = X.values 

### Dividing Dataset to the training and testing sets 
from sklearn.model_selection import train_test_split
X_train, X_test, L_train, L_test = train_test_split(X,L,test_size=0.3)

### Standardization on training and testing sets 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

### Loading an KNN Model 
from sklearn.neighbors import KNeighborsClassifier
Model = KNeighborsClassifier(n_neighbors=3) 

### Training the model 
Model.fit(X_train,L_train)

### Predicting the testing samples 
Pre = Model.predict(X_test)
Score = Model.score(X_test,L_test)
