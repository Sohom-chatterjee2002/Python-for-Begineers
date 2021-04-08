# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:22:11 2020

@author: Sohom Chatterjee_CSE1_T25
"""

#Given two strings, s1 and s2 return a new string made of the first,middle,last char each input string.
def mix_string(s1,s2):
    first_char=s1[:1]+s2[:1]
    middle_char=s1[int(len(s1)/2):int(len(s1)/2)+1]+s2[int(len(s2)/2):int(len(s2)/2)+1]
    last_char=s1[len(s1)-1]+s2[len(s2)-1]
    res=first_char+middle_char+last_char
    return res
s1=input("Enter your first string: ")
s2=input("Enter your second string: ")
print(mix_string(s1,s2))