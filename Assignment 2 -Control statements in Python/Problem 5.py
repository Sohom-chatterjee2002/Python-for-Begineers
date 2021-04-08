# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:38:00 2020

@author: Sohom Chatterjee_CSE1_T25
"""

# Write a python program to print pattern.
side=int(input("Please enter any side of the sqaure: "))
print("Hollow sqaure pattern: \n")
i=0
while(i<side):
    j=0
    while(j<side):
        if(i==0 or i==side-1 or j==0 or j==side-1):
            print('*',end='  ')
        else:
            print(' ',end='  ')
        j=j+1
    i=i+1
    print()