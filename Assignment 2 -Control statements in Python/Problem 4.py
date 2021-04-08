# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:31:26 2020

@author: Sohom Chatterjee_CSE1_T25
"""

# Write a python program to print pattern.
rows=int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(-1+i,-1,-1):
        print(format(2**j, "4d"),end='  ')
    print("")