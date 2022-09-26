# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:56:39 2020

@author: Reza
"""

X = 5 
Y = 10 
C = X + Y 
D = Y / X 
E = Y // X 
A = X - Y 
print(C,D,E,A)

X = 5.0 
print(type(X))
X1 = 2 + 8j 
print(type(X1))
X1 = X1.conjugate()
print(X1.real)
print(X1.__abs__())
print(X1.imag)

D = X**3
print(D)

Text = "reza" 
print(type(Text))
print(Text.capitalize())
Text1 = " Akbari Movahed" 
Text2 = Text + Text1
print(Text2)
print(Text2.count('e'))
print(Text2.isnumeric())

C0 = False 
C1 = True 
print(not(C0))
print((C0 and C1))
print((C0 or C1))

S = X < Y 
print(S)
print(X<=Y)
print(X>Y)
print(X>=Y)
print(X==Y)
print(X!=Y)





