# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:21:51 2020

@author: Reza
"""

import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)

## Plot the points using matplotlib
fig = plt.figure() 
plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sin')
plt.show()
fig.savefig('E:\\My Cources\\Machine Learning With Python\\991\\Jalase 9\\Fig.jpg')

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x,y_sin,'r*')
plt.plot(x,y_cos,'bo')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sin and Cos')
plt.legend(['Sin','Cos'])
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y_sin,'y')
plt.title('Sin')
plt.subplot(1,2,2)
plt.plot(x,y_cos,'g')
plt.title('Cos')
plt.show()

x1 = np.linspace(0,2,100)
plt.plot(x,x,label='linear')
plt.plot(x,x**2,label='quadratic')
plt.plot(x,x**3,label='cubic')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Plot')
plt.legend()
plt.show()

E = np.random.randint(1,9,size=(3,4))
E1 = np.reshape(E,(1,12))
E2 = np.reshape(E,(2,6))

List1 = [[3,2],[1,8],[5,9]]

Array1 = np.asarray(List1)

D = np.logspace(0,10,base=100.0)


f = np.array([1,2,3])
g = np.array([4,5,6])

H = np.hstack((f,g))
V = np.vstack((f,g))

a = np.array([[1,2],[3,4]])
b = np.array([[6,7],[5,2]])

A = np.concatenate((a,b),axis=0)
B = np.concatenate((a,b),axis=1)




