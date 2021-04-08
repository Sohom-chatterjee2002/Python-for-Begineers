# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:53:41 2020

@author: Sohom Chatterjee_CSE1_T25
"""

# Represent an integer to roman number.
class solution:
    def integer_to_roman(self,num):
        value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbol=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        roman_num=''
        i=0
        while(num>0):
            for _ in range(num//value[i]):
                roman_num+=symbol[i]
                num-=value[i]
            i+=1
        return roman_num

n=int(input("Enter your integer: "))
print(solution().integer_to_roman(n))

#Input- 25
#Output- XXV