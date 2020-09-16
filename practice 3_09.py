# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:02:06 2020

@author: Deep Chokshi
"""

"""
def check_range(num1,start,stop):
    if num1 >= start and num1 <=stop:
        print ("Yes it is in range")
    else:
        print ("Out of range")

start = int(input("Enter starting range"))
stop = int(input("Enter end of range"))
num1 = int(input("Enter number to check it is in range"))
check_range(num1,start,stop)
    """
    
"""
def check_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num%i)== 0:
                print ("Not prime")
                break
        else:
            print("Number is prime")
    else:
        print ("Not prime")
        
number = int(input("Enter number to check it is prime or not:"))
check_prime(number)
"""
"""
def check_palin(string):
    pal = ""
    for i in string:
        pal = i + pal
    if pal == string:
        print ("It is palindrome")
    else:
        print ("Nor palindrome")

string = input("Enter sting to check palindrome")
check_palin(string)
"""
def check_peferct_num(num):
    sum=0
    for i in range(1,num):
        if num%i ==0:
            sum = sum + i
    if sum == num:
        print ("Perfect number")
    else:
        print ("Not perfect number")

number = int(input("Enter number to check it is perfect or not:"))
check_peferct_num(number)
            
