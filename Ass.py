# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:30:02 2020

@author: Deep Chokshi
"""


menu = {1:("soup",200),2:("Sabji",370),3:("Bread",30),4:("Rice",200),5:("Dal",175)}
for i in menu:
    name,price=menu[i]
    print ("Press "+str(i)+" for "+name+" Rupees."+str(price))
customer_choice=[]
Final_amount=0
print ("Press 0 for exit the menu:")

while True:
    choice = int(input("Enter the your choice:"))
    if choice == 0:
        break
    elif choice not in menu:
        print ("Please order from the menu only")
    else:
        quantity = int(input("Enter no. of dish:"))
        Final_amount = Final_amount + (quantity * menu[choice][1])

print ("Your Total bill is:"+str(Final_amount))