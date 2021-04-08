# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:23:56 2020

@author: Sohom Chatterjee_CSE1_T25
"""

# Find all occurences of "India" in given string ignoring the case.
s=input("Please enter your string: ")
substring=input("Enter your substring which you want to search: ")
tempstring=s.lower()
count=tempstring.count(substring.lower())
print("Your substring occurence is in your inputted string: ",count)