# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:26:19 2020

@author: Sohom Chatterjee_CSE1_T25
"""

#Write a python program to print the prime factors of an integer.
n=int(input("Enter an integer: "))
print("Factors are: ")
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1