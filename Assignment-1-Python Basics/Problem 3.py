# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:23:03 2020

@author: Sohom Chatterjee_CSE1_T25
"""

def append_middle(s1,s2):
    middleIndex=int(len(s1)/2)
    print("Original strings are: ",s1,s2)
    middleThree=s1[:middleIndex]+s2+s1[middleIndex:]
    print("After appending new string in middle: ",middleThree)
s1=input("Enter your first string: ")
s2=input("Enter your seccond string: ")
append_middle(s1,s2)