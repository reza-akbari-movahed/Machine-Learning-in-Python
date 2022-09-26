# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:33:17 2020

@author: Reza
"""

import numpy as np
import sklearn as sk 
from mlxtend.feature_selection import SequentialFeatureSelector as SFS 

#### Loading Iris Dataset 
from sklearn.datasets import load_iris
X,L = load_iris(return_X_y=True) 

### Dividing Dataset to the training and testing sets 
from sklearn.model_selection import train_test_split
X_train, X_test, L_train, L_test = train_test_split(X,L,test_size=0.3)

### Feature Selection 
from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors=1)
sfs1 = SFS(knn,
           k_features = 4, 
           forward = True,
           cv = 5)
sfs1.fit(X_train,L_train)
Results = sfs1.subsets_
SF = Results[3]['feature_idx']
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt 
fig = plot_sfs(sfs1.get_metric_dict())

### Removing nonselected features 
X_train = X_train[:,SF]
X_test = X_test[:,SF]

### Normalization on training and testing sets 
X_train = (X_train-np.min(X_train))/(np.max(X_train)-np.min(X_train))
X_test = (X_test-np.min(X_test))/(np.max(X_test)-np.min(X_test))

### Loading LDA Classifier 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
Model = LinearDiscriminantAnalysis()

### Training the classifier model 
Model.fit(X_train,L_train)

### Predicting the testing samples
Predict = Model.predict(X_test)

### Evaluting the model 
Score = Model.score(X_test,L_test)
