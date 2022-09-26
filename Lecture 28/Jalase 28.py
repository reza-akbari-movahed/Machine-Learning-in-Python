# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:15:02 2020

@author: Reza
"""

import numpy as np 
import keras as ke 
from keras.models import Sequential 
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD 
import cv2 
from keras.callbacks import EarlyStopping

### Initial Settings of training network 
Epochs = 2 
bacth_size = 128  
num_classes = 10 

(X_train,L_train),(X_test,L_test) = ke.datasets.mnist.load_data()
cv2.imshow('Image',X_train[0,:,:])
cv2.waitKey(0)
cv2.destroyAllWindows()
X_train = X_train.reshape(60000,28*28)
X_test = X_test.reshape(10000,28*28)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train = (X_train-np.min(X_train))/(np.max(X_train)-np.min(X_train))
X_test = (X_test-np.min(X_test))/(np.max(X_test)-np.min(X_test))

L_train = ke.utils.to_categorical(L_train)
L_test = ke.utils.to_categorical(L_test) 

model = Sequential()
model.add(Dense(512,input_dim=784))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes))
model.add(Activation('softmax'))

model.summary()

### Configuring the settings of the training process of the model 
model.compile(SGD(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics = ['accuracy'])

es = EarlyStopping(monitor='val_loss')

model.fit(X_train,L_train,validation_split=0.2,
          epochs=Epochs, batch_size=bacth_size,callbacks=[es])

Pre = model.predict_classes(X_test)

Score = model.evaluate(X_test,L_test)
print('Test Accuracy: ', Score[1])
print('Test Loss: ', Score[0])
