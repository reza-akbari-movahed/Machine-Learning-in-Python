# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:37:55 2020

@author: Reza
"""


sequences = [] 
for i in range(0,3):
    sequences.append(i**2)
    
del i, sequences

sequences = [i**2 for i in range(0,3)]
### Tuples 

thistuple = (15,-63.24,12+5j,"HUT",False,"Bannana","Apple")
print(thistuple)
print(type(thistuple))
print(thistuple[0],"\n",thistuple[2],"\n",thistuple[5])

import time as TT

for i in range(len(thistuple)):
    TT.sleep(0.5)
    print(thistuple[i])
    
print(thistuple[-1],"\t",thistuple[-3],"\t",thistuple[-6])


thistuple.count(15)
thistuple.index(False)

A = 15 not in thistuple 

thistuple[0] = 23 

thislist = list(thistuple)
thislist[0] = 23
thislist.append("~")

T1 = (1,2,3,4,5)
T2 = ('a','b','c')
T3 = T1 + T2 
print(T3)
print(T1[0:3])
print(T1[-5:-1])

T4 = (T2,T1,[1,2,3])
L1 = [T2,T1,["apple",12]]

for i in thistuple:
    TT.sleep(0.5)
    print(i)
print("The Loop is finished")

### Dictionary 

thisdict = {"Reza":27,"Zahra":32,"Behdad":45}
print(len(thisdict))
print(thisdict["Reza"],"\t",thisdict["Behdad"],"\t",thisdict["Zahra"])
print(thisdict)
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

A = tuple(thisdict.keys())

for x in thisdict.keys():
    TT.sleep(0.5)
    print(x,"\t",thisdict[x])
    
for x,y in thisdict.items():
    TT.sleep(0.50)
    print(x,y)
 
