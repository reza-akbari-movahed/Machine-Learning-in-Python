# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 10:09:32 2020

@author: Reza

"""

def Evaluate(predict,Label):
    N = Label.shape[0]
    H = predict == Label
    Nt = np.sum(H==1)
    Accurcy = Nt/N 
    Loss = 1 - Accurcy 
    return Accurcy, Loss 
    

import numpy as np 
import sklearn as sk 


### Loading breast cancer dataset 
from sklearn.datasets import load_breast_cancer 
X,L = load_breast_cancer(return_X_y=True) ## L=1 Benign, L=0 Malignant 
print("The Number of Malignant Samples is: ", np.sum(L==1))
print("The Number of Benign Samples is: ", np.sum(L==0))

### Dividing Dataset to the training and testing sets 
from sklearn.model_selection import train_test_split
X_train, X_test, L_train, L_test = train_test_split(X,L,test_size=0.3)

### Standardization on training and testing sets 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

### Loading an QDA Model 
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
Model = QuadraticDiscriminantAnalysis()

### Training the QDA Model 
Model.fit(X_train,L_train)

### Testing the trained model 
Predict = Model.predict(X_test)

### Evaluating the Model 
Accurcy, Loss = Evaluate(Predict,L_test)
