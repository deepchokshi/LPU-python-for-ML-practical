# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:00:49 2020

@author: Deep Chokshi
"""


"""fruit = "banana"
i =0
while i < len(fruit):
    print (fruit[i])
    i = i+1
    """
from string import *

stri = input("Enter your mobile number:")
if stri.isdigit() and len(stri) == 10:
    print ("Valid mobile number")
else:
    print ("Please enter valid number")