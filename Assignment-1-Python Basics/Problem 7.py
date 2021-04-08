# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:11:17 2020

@author: Sohom chatterjee , CSE1_T25
"""

#Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list.
l=[]
n=int(input("Enter the number of element: "))
print("Enter your element: ")
for i in range(0,n):
    element=int(input())
    l.append(element)
y=l[4]
l.remove(4)
l.insert(2,y)
l.insert(n,y)
print("After operation your output list is: \n")
for i in range(0,n):
    print(i)