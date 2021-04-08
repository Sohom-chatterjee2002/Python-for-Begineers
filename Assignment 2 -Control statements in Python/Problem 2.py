# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:19:41 2020

@author: Sohom Chatterjee_CSE1_T25
"""

# Write a python program to check whether a number is a palindrome or not.
num=int(input("Enter your number: "))
temp=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if(temp==rev):
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")