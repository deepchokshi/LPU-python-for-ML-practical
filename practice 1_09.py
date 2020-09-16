# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:01:42 2020

@author: Deep Chokshi
"""


"""def even_odd(x):
    if x%2 ==0:
        print ("Even")
    else:
        print ("Odd")

number = int(input("enter number to check number even or odd:"))
even_odd(number)
"""
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

num = int(input("Enter the number to check the factorial of a number:"))

if num < 0:
   print("nagative number")
elif num == 0:
   print("The factorial of",num," is 1")
else:
   print("The factorial of", num, "is", factorial(num))