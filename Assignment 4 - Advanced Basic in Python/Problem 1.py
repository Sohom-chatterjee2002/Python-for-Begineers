
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:57:27 2020

@author: Sohom Chatterjee_CSE1_T25
"""

# Reduce a string problem
i =input("Enter your string: ")
s = []
for c in i:
    if(not s):
        s.append(c)
    else:
        if(s[-1] == c):
            s.pop()
        else:
            s.append(c)
            
if(not s):
    print("Empty String")
else:
    print(''.join(s))
    
#Input- aaabccddd
#Output- abd
