# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:21:23 2020

@author: Deep Chokshi
"""


# Write a program in python to reverse a string.
string = input("Enter the string:")
rev_string = ""
for i in string:
    rev_string = i + rev_string
print (rev_string)


#Write a program in python to check whether a given string is palindrome or not
string = input("Enter the string to check Palindrome:")
rev_string = ""
for i in string:
    rev_string = i + rev_string
if rev_string == string:
    print ("Your string is Palindrome")
else:
    print ("Your string is not Palindrome")



"""Write a Python function that accepts a string and calculate the number of 
upper case letters and lower case letters"""
string = input("Enter the string:")
upper=0
lower=0
for i in string:
    if i.isupper():
        upper +=1
    if i.islower():
        lower +=1
print ("No. of UPPER case character:",upper)
print ("No. of lower character:",lower)


#