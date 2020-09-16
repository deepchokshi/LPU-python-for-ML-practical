# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 09:56:01 2020

@author: Deep Chokshi
"""


##Creation of list and changing value of any one element, also display the length of list
list1 = []
num = int(input("Enter how many elemnts you want to add to list:"))
for i in range (1,num+1):
    n = int(input("Enter the elemnt {}:".format(i)))
    list1.append(n)

print ("List before changing the element",list1)
index = int(input("Enter index to change value:"))
value = int(input("Enter the new value:"))
list1[index] = value
print ("List after changing the element",list1)


## Create a list and append two elements in it
list1=[]
for i in range(2):
    value = int(input("Enter the elemtn:"))
    list1.append(value)
print (list1)


## Create a list and sort it.
list1=[]
num = int(input("Enter how many elemnts you want to add to list:"))
for i in range (1,num+1):
    n = int(input("Enter the elemnt {}:".format(i)))
    list1.append(n)
list1.sort()
print (list1)


## Create a list of numbers and print sum of all the elements
num = int(input("Enter how many elemnts you want to add to list:"))
sum=0
for i in range (1,num+1):
    n = int(input("Enter the elemnt {}:".format(i)))
    list1.append(n)
for i in list1:
    sum += i
print (sum)



## Program to compare elements of list.
list1=[1,3,4,9,8]
list2=[7,6,2,1,5]
common=[]
notcommon=[]
for i in list1:
    if i in list2:
        common.append(i)
    else:
        notcommon.append(i)
print ("Common Elemnts are:",common)
print ("Unique Elemnts are:",notcommon)



##Program to find maximum and minimum of list.
num = int(input("Enter how many elemnts you want to add to list:"))
for i in range (1,num+1):
    n = int(input("Enter the elemnt {}:".format(i)))
    list1.append(n)
larger=0
smaller = list1[0]
for i in range(len(list1)):
    if larger < list1[i]:
        larger = list1[i]
    if smaller > list1[i]:
        smaller = list1[i]
print ("Maximum number is",larger)
print ("Minimum number is",smaller)

        

## Count the occurrence of element in list
list1=[1,5,3,1,5,8,9,9,9]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
        count = list1.count(i)
        print (i,"comes",count)


##Reverse a list
list1=[11,45,23,78,3]
rev_list=[]
for i in list1[-1::-1]:
    rev_list.append(i)
print (rev_list)



"""Write a loop that traverses the previous list and prints the length of each 
element. What happens if you send an integer to len?"""
for i in rev_list:
    print (len(i)) #We will get error of int object has no len()
    



"""Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given
list of strings"""

str_list=["aba","deep","bab","a","did"]
count=0
for i in str_list:
    if len(i) >= 2 and i[0] == i[-1]:
       count+=1
print (count)