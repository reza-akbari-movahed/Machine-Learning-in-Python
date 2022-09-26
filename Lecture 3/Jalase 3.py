# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:02:22 2020

@author: Reza
"""

L1 = ["HUT",12-6j,56.37,False]
print(L1[-1],"\n",L1[-2],"\n",L1[-3],"\n",L1[-4])

import math as m

print(m.pow(5,2))

List1 = []
List2 = [] 
for i in range(0,9):
    List1.append(i)
    List2.append(m.pow(i,2))
print("The Loop is finished")


import time as TT
List3 = [[1,2],[3,4],[5,6]]

for i in range(len(List3)):
    for j in range(len(List3[i])):
        TT.sleep(0.5)
        print(List3[i][j])
print("The Loop is finished")

L1[0] = "Reza"
L1[1] = True
L1[2] = 58.32 

if "HUT" in L1:
    print("HUT is in this list")
elif (12-6j) in L1:
    print(12-6j," is in this list")
elif 58.32 in L1: 
    print(58.32," is in this list")
else:
    print("None of the items is not in this list")
    
L1.pop(0)

p = 10 
P = [] 
while p>=0:
    P.append(m.factorial(p))
    p = p - 1
print("The Loop is finished")

X1 = list(range(1,9,2))
X2 = list(range(1,10,1))
X = [X1,X2]
I = 0 

for i in range(len(X)):
    for j in range(len(X[i])):
        TT.sleep(0.5)
        a = X[i][j]
        if a==3:
            I = I + 1 ; 
            print("The Number 3 is found in X")
print("The Loop is Finished")
print("The Iteration number of 3 is ",I)

a1 = [10,8,5]
a2 = [1,-2,-7]
a3 = a1 + a2 
print(a3)

for x in a3: 
    if x==-2:
        break
    print(x)
print("The Loop is finished")

for x in a3: 
    if x==-2:
        continue
    print(x)
print("The Loop is finished")
