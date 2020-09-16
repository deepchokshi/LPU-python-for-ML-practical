# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:28:40 2020

@author: Deep Chokshi
"""


"""string = input("Enter the string:")
dic={}
value=1
for i in string:
    dic[i] = value
    value+=1
print (dic)"""

dic={"positive":0,"negative":0}
def histogram(list1):
    for i in list1:
        if i >=0:
            dic['positive'] += 1
        else:
            dic["negative"] +=1
    return dic

list1 = []
num = int(input("Enter how many elemnts you want to add to list:"))
for i in range (1,num+1):
    n = int(input("Enter the elemnt {}:".format(i)))
    list1.append(n)
print (histogram(list1))
            