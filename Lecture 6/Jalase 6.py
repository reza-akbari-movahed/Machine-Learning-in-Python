# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:44:59 2020

@author: Reza
"""
import math as m

def my_function():
    print("Hello From a Function")
    
    
def Nationality(country):
    if type(country)!= str:
        print("Your Input Format is Wrong")
    else:
        print("Your Nationality is " + country+'ian' )
        A = "Your Nationality is " + country+'ian' 
    return A

def Solve_EQN2(X):
    if (type(X)!=list) or (len(X)!=3):
        print("Your Input Format is Wrong")
    else:
        a = X[0]
        b = X[1]
        c = X[2]
        Delta = m.pow(b,2) - 4*a*c
        if Delta>0:
            R1 = (-b+m.sqrt(Delta))/(2*a)
            R2 = (-b-m.sqrt(Delta))/(2*a)
            R = [R1,R2]
        elif Delta==0:
            R1 = (-b/(2*a))
            R = [R1]
        else:
            print("This Equation has not any real root")
            R=[]
    return R

def my_function1(*kids):
    print("The youngest child is " + kids[-1])
    
def my_function2(**kids):
    print("His last name is " + kids['lname'])


my_function()
Nationality("Iran")
Nationality(2)
O1 = Nationality("Iran")
S = Solve_EQN2([1,0,-1])

my_function1('Reza','John',"Emmy",'Hadi')
my_function2(fname="Reza",lname="Akbari Movahed")

S = input("Please Enter a number")

x1 = ('apple','bannana','cherry')
y = enumerate(x1)
Y = list(y)

for i in Y:
    print(i[0],'->',i[1])
