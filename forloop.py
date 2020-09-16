# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:17:01 2020

@author: Deep Chokshi
"""


amount = 10000
roi = 0.06
period = 5
inital_amt = amount
for i in range(period):
    final_amount = inital_amt * roi
    print ("You beginning amount is:"+str(inital_amt)+" and you earn interest:"+
           str(final_amount-inital_amt))
    inital_amt = final_amount
    
print  ("You final amount after"+str(period)+" is:"+str(final_amount)+
        " and you earn interest:"+str(final_amount-amount))