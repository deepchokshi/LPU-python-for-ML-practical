# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:21:01 2020

@author: Deep Chokshi
"""


'''string = input("Enter the string")
for i in string:
    if i.isalpha():
        print (i,"index is:",string.index(i))
'''

'''def square(r):
    dic={}
    for i in range(1,r+1):
        dic[i] = i**2
    return dic

range_sq=int(input("Enter the range for square:"))
print (square(range_sq))'''

vowel = ['a','e','i','o','u']
string = input("Enter the string:")
count=0
for i in string:
    if i in vowel:
        count+=1
print ("Total vowels are:",count)