# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:23:23 2020

@author: Reza
"""

import os 
import numpy as np
import cv2 

print(os.cpu_count())
print(os.getcwd())

Dir = os.listdir(os.getcwd())
os.makedirs(os.getcwd()+'\\new')
print(os.path.join(os.getcwd(),'new'))

I = cv2.imread('E:\My Cources\Machine Learning With Python\991\Jalase 10\Cat.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image',I)
cv2.waitKey(0)
cv2.destroyAllWindows()
img_neg = 255 - img


Img_Dataset = [] 
Img_labels = [] 
Link = 'E:\My Cources\Machine Learning With Python\991\Jalase 10\DigitDataset'
List0 = os.listdir(Link)
for eachfolder in List0:
    Each_Path = os.path.join(Link,eachfolder)
    print(Each_Path)
    Each_Path_Files = os.listdir(Each_Path)
    for eachfile in Each_Path_Files:
        Full_link = os.path.join(Each_Path,eachfile)
        Img = cv2.imread(Full_link,cv2.IMREAD_GRAYSCALE)
        Img_Dataset.append(Img)
        Img_labels.append(int(eachfolder))
        
Img_Store = np.asarray(Img_Dataset)
Img_Labels = np.asarray(Img_labels)
