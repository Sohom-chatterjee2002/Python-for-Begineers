# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:03:54 2020

@author: Sohom Chatterjee_CSE1_T25
"""

#Given a string of length greater than 2, return a string except 1st and last characters.
def new_string(s):
    new_str=s[1:-1]
    return new_str
s=input("Enter your string: ")
print(new_string(s))
