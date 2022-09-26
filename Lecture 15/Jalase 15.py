# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:33:31 2020

@author: Reza
"""

def Evaluate_CM(L_test,Predict):
    NTP = 0 
    NTN = 0 
    NFP = 0 
    NFN = 0 
    for i in range(Predict.size):
        if (Predict[i]==0)and(L_test[i]==0):
            NTP = NTP + 1
        elif (Predict[i]==1)and(L_test[i]==1):
            NTN = NTN + 1 
        elif (Predict[i]==0)and(L_test[i]==1):
            NFP = NFP + 1 
        else:
            NFN = NFN + 1 
    Accuracy = (NTP+NTN)/(NTP+NTN+NFP+NFN)
    Sensitivity = NTP/(NTP+NFN)
    Specificity = NTN/(NTN+NFP)
    F1 = (2*NTP)/((2*NTP)+NFP+NFN)
    Loss = 1 - Accuracy
    return Accuracy, Sensitivity, Specificity, F1, Loss 


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
Accuracy, Sensitivity, Specificity, F1, Loss =  Evaluate_CM(L_test,Predict)
