# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:32:37 2020

@author: Reza
"""

import numpy as np 
import sklearn as sk
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris 


X,L = load_iris(return_X_y=True)


G1_ind = L == 0
G2_ind = L == 1
G3_ind = L == 2

G1 = X[G1_ind,:]
G2 = X[G2_ind,:]
G3 = X[G3_ind,:]


data = (G1,G2,G3)
groups = ("Setosa","Versicolour","Virginica")
colors = ('red','green','blue')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

A = list(zip(data,groups,colors))

for Data,group,Color in zip(data,groups,colors):
    x = Data[:,0]
    y = Data[:,1]
    ax.scatter(x,y,c=Color,s=30,label=group)
    
plt.title('Scatter Plot')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.legend()
plt.show()
