# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:11:06 2020

@author: Sohom Chatterjee_CSE1_T25
"""

#Write a python program to find the smallest divisor of an integer other than 1.
n=int(input("Enter an integer: "))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor(other than 1) is: ",a[0])
