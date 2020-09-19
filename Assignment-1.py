# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:52:58 2020

@author: Deep Chokshi
"""
"""""
#Assignment @uestion 1 
def all_combination(list1, count, length): 
    if count==length: 
        print("".join(list1))
    else: 
        for i in range(count,length+1): 
            list1[count], list1[i] = list1[i], list1[count] 
            all_combination(list1, count+1, length) 

if __name__ == "__main__":
    string = input("Enter the string of lenght 4:")
    length = 4 
    list1 = list(string) 
    all_combination(list1, 0, length-1) 
"""""
"""""
#Assignment 1 Question 2
def sort(list1):
    for i in range (len(list1)):
        for j in range(i + 1, len(list1)):
            if(list1[i] > list1[j]):
                list1[i],list1[j] = list1[j],list1[i]
    return list1
if __name__ == "__main__":
    string = input("Enter the string:")
    list1 = []
    for i in string:
        if i.isdigit() and i not in list1:
            list1.append(i)
    sorted_list = sort(list1)
    result =""
    for i in sorted_list:
        result = result + i

print (" ".join(result))
"""


#Assignment 1 Question 3
menu = {1:("soup",200),2:("Sabji",370),3:("Bread",30),4:("Rice",200),5:("Dal",175)}
for i in menu:
    name,price=menu[i]
    print ("Press "+str(i)+" for "+name+" Rupees."+str(price))
customer_choice=[]
Final_amount=0
print ("Press 0 for exit the menu:")

while True:
    choice = int(input("Enter your choice:"))
    if choice == 0:
        break
    elif choice not in menu:
        print ("Please order from the menu only")
    else:
        quantity = int(input("Enter no. of dish:"))
        Final_amount += quantity * menu[choice][1]

print ("Your Total bill is:"+str(Final_amount))
