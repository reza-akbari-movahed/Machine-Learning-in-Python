# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:58:57 2020

@author: Reza
"""

import numpy as np

a = np.array([1,2,3])
print(a)
print(type(a))
print(a[0],a[1],a[2])
a[0]=5


b = np.array([[1,2,3],[4,5,6]])
b.argmax()
b.max()
Sh = b.shape

print(b[0,0],b[1,0],b[0,1])

for i in range(Sh[0]):
    for j in range(Sh[1]):
        #print(b[i,j])
        print(b[i][j])
        
print('The Loop is finished')

a0 = np.zeros((2,2),dtype=np.int16)
b0 = np.ones((3,4),dtype=np.int64)
print(b0)
d0 = np.eye(5)
print(d0)
e = np.random.random((6,5))

A = np.random.randint(5,size=(2,3,4))
print(A[0,:,:])
print(A[1,:,:])

print(np.shape(e))
print(e[1:4,:])
print(e[:,0:3])
print(e[0:2,1:4])

print(A[0,0:2,:])

print(A[0,:,1:])

print(A[0,:2,1:])


a = np.random.randint(6,size=(3,2))
b = np.random.randint(4,size=(3,2))
c = a + b # np.add(a,b) 
c = a * b # np.multiply(a,b)
c0 = np.dot(a,b.transpose())

c1 = a/b # np.divide(a,b)

np.sum(A,axis=0)
np.sum(A,axis=1)
np.sum(A,axis=2)


a_new = np.reshape(a,(1,6))
print(a_new)
E = np.reshape(a_new,(3,2))


print(a0.ndim)
print(a_new.ndim)
print(A.ndim)

print(A.mean()) ## np.mean(A)
print(A.std()) ## np.std(A)

S = E > 4 

S0 = E <= 2 
