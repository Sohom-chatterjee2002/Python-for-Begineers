# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:38:20 2020

@author: Sohom Chatterjee_CSE1_T25
"""

# Find the twins prime.
def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def twins_prime(start,end):
    for i in range(start,end):
        j=i+2
        if(is_prime(i) and is_prime(j)):
            print("{:d} and {:d}".format(i,j))

low=int(input("Enter your lower range: "))
high=int(input("Enter your higher range: "))
print(twins_prime(low,high))


#Input: Enter lower range: 3, Enter higher range: 50
#Output: 3 and 5, 5 and 7, 11 and 13, 17 and 19, 29 and 31, 41 and 43, None