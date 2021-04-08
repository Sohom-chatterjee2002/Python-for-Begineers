# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:18:05 2020

@author: Sohom Chatterjee_CSE1_T25
"""

def decimal_to_binary(dec):
    decimal=int(dec)
    print(decimal, " in binary: ",bin(decimal))

def decimal_to_octal(dec):
    decimal=int(dec)
    print(decimal, " in octal: ",oct(decimal))
def decimal_to_hexadecimal(dec):
    decimal=int(dec)
    print(decimal, " in hexadecimal: ",hex(decimal))

dec=input("Enter your decimal number: ")
print("BASE VALUE CHART")
print("-----------------")
print("1. DECIMAL TO BINARY---> BASE= 2")
print("2. DECIMAL TO OCTAL---> BASE= 8")
print("3. DECIMAL TO HEXADECIMAL---> BASE=16")
print("----------------------------------------")
base=int(input("Enter your base value according to BASE VALUE CHART: "))
if(base==2):
    decimal_to_binary(dec)
elif(base==8):
    decimal_to_octal(dec)
elif(base==16):
    decimal_to_hexadecimal(dec)
else:
    print("Please enter correct base value.")        