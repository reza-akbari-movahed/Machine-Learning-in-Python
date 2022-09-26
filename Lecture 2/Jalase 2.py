# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:53:57 2020

@author: Reza
"""

A = "mohammad" 
print(A.capitalize())
print(A.upper())

print(A[0],"\n",A[1],"\n",A[3])
print(len(A))

import time as TT

for i in A:
    TT.sleep(0.5)
    print(i)
print("The Loop is finished")

a = 60 
b = 13 
c = 0 

c = a & b 
c = a | b 
c = a ^ b 
c = ~a
c = a << 2
c = a >> 2 

print("m" in A)
print(not("e" in A))
print("e" not in A)
a_b = bin(a)
print(a_b)
a_h = hex(a)
print(a_h)

List1 = ["Reza",12.54,64,1+6j,True]
print(len(List1))
print(List1[0],"\t",List1[1],"\t",List1[2],"\t",List1[3],"\t",List1[4])
List1.append("HUT")
List1.insert(0,-15)
List1.count("Reza")
List1.index(12.54)
List1.remove(64)
R = list(range(5))
R1 = list(range(1,5))

for j in range(len(List1)):
    TT.sleep(0.5)
    print(j,"\t",List1[j])
    
    
for x in List1:
    TT.sleep(0.5)
    print(x)
    
D = int(65.21)
D1 = float(90)
D2 = str(D1)
D3 = bool(0)

A1 = input("Enter a number between 0 and 8")
