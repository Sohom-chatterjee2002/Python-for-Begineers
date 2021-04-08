# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:25:28 2020

@author: Sohom Chatterjee_CSE1_T25
"""

#The set of input is given as ages. then print the status according to rules.
def age_status(age):
    if(age<=1):
        print("in_born")
    elif(age>=2 and age<=10):
        print("child")
    elif(age>=11 and age<=17):
        print("young")
    elif(age>=18 and age<=49):
        print("adult")
    elif(age>=50 and age<=79):
        print("old")
    else:
        print("very_old")
age=int(input("Enter your age: "))
age_status(age)