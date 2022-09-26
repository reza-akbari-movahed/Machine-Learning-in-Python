# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:58:22 2020

@author: Reza
"""

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
        
ozzy = Dog("Ozzy",2)
print(ozzy.age)
print(ozzy.name)
print(ozzy.name + ' is ' + str(ozzy.age) + ' years old')


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("bark bark!!")
        
        
ozzy = Dog("Ozzy",2)
ozzy.bark()

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("bark bark!!")
        
    def doginfo(self):
        print(self.name + ' is ' + str(self.age) + ' years old')
        
ozzy = Dog("Ozzy",2)
ozzy.doginfo()
Fili = Dog('Fili',5)
Ara = Dog('Ara',6)

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("bark bark!!")
        
    def doginfo(self):
        print(self.name + ' is ' + str(self.age) + ' years old')
        
    def birthday(self):
        self.age += 1 
        
ozzy = Dog("Ozzy",2)
print(ozzy.age)
ozzy.birthday()
print(ozzy.age)


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("bark bark!!")
        
    def doginfo(self):
        print(self.name + ' is ' + str(self.age) + ' years old')
        
    def birthday(self):
        self.age += 1 
        
    def setBuddy(self,buudy):
        self.buudy = buudy
        buudy.buudy = self
        
Ozzy = Dog('Ozzy',2)
Far = Dog('Far',3)

Ozzy.setBuddy(Far)

Ozzy.buudy


X = [12,32,'Reza']

S = 'Hamedan'
