# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:04:19 2020

@author: Reza
"""

### Importing the required modules 
import numpy as np 
import keras as ke 
from keras.models import Sequential 
from keras.layers import Dense, Activation
from keras.optimizers import SGD 

## Generate Random Dataset 
X_train = np.random.random((1000,20))
L_train = np.random.randint(2,size=(1000,1))
X_test = np.random.random((100,20))
L_test = np.random.randint(2,size=(100,1))

L_train = ke.utils.to_categorical(L_train)
L_test = ke.utils.to_categorical(L_test) 

### Defining layers of the MLP model 
model = Sequential()
model.add(Dense(64,input_dim=20))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(2))
model.add(Activation('softmax'))

### Configuring the settings of the training process of the model 
model.compile(SGD(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics = ['accuracy'])

### Training the model 
model.fit(X_train,L_train,
          epochs=5, batch_size=128)

### Applying Testing samples on the trained model 
Pre = model.predict_classes(X_test) 

Sp = model.predict(X_test)
