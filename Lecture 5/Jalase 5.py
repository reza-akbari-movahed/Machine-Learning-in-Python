# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:21:45 2020

@author: Reza
"""

thisdict = {"brand":"Ford","Model":"Mustang","Year":1987}

import time as TT

for x in thisdict:
    TT.sleep(0.5)
    print(x,"\t",thisdict[x])
    
thisdict["brand"] = "BMW" 
thisdict.pop("Model")
thisdict.clear()
thisdict.update({'color':'Blue'})
Dict1 = dict(brand="Ferarri",Year=1999)
Dict1.get('brand') 

List1 = [12,-90,"reza"]
List2 = List1 
List1.append("HUT")
del(List2)

List2 = List1.copy()
List1.append(5+2j)

thisdict1 = thisdict.copy()
thisdict.update({"Speed":190})

myfamily = {
        'Child1':{"Name":"Reza","Age":27},
        'Child2':{"Name":"Mohammad","Age":32},
        'Child3':{"Name":"Zahra","Age":18}}

for x in myfamily:
    print(x)
    print('-------------------')
    for y in myfamily[x]:
        TT.sleep(0.5)
        print(myfamily[x][y])
        
#### Set ##### 
thisset = {'apple',25,-78.54,('A','a')}
print(thisset)
print(len(thisset))
print(type(thisset))
set1 = {12,-96,"Reza",12}
print(set1)

for x in thisset:
    TT.sleep(0.5)
    print(x)
    
    
thisset.add('Orange')
print(thisset)
thisset.update([True,-45,20])
print(thisset)
thisset.remove(20)        
thisset.clear()
set2 = set([10,20,30,10])
set3 = set([10,5,30,15])
set4 = set3.union(set2)
set5 = set3.intersection(set2)
print(set5)
print(set4)
print(set2)
