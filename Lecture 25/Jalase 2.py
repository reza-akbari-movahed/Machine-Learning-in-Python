# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:33:01 2020

@author: Reza
"""

### K-means clustring example 
import numpy as np 
from matplotlib import pyplot as plt 
from sklearn.datasets.samples_generator import make_blobs 
from sklearn.cluster import KMeans 

### Data Generation 
X,Y = make_blobs(n_samples=300,n_features=2, 
                 centers=4,cluster_std=0.6)
plt.scatter(X[:,0],X[:,1])

### Applying K-means clustring on the generated data 
k_means = KMeans(n_clusters=4)
pred_y = k_means.fit_predict(X)

plt.scatter(X[:,0],X[:,1])
plt.scatter(k_means.cluster_centers_[:,0],k_means.cluster_centers_[:,1],
            s=300,c='red')
plt.show()

X_0 = X[pred_y==0,:]
X_1 = X[pred_y==1,:]
X_2 = X[pred_y==2,:]
X_3 = X[pred_y==3,:]
