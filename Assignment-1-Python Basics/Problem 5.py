# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:51:08 2020

@author: Sohom Chatterjee_CSE1_T25
"""

# Find the last position of the substring "Emma" in given string.
str1=input("Enter your original string: ")
str2=input("Enter your substring: ")
print("Your original string is: ",str1)

index=str1.rfind(str2)
print("last occurence of Emma starts at: ",index)