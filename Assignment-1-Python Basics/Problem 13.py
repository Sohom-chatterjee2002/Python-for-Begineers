# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:53:12 2020

@author: Sohom Chatterjee_CSE1_T25
"""

#Modify the first item (22) of a list inside a following tuple to 222 tuple1 = (11, [22,33], 44, 55)
tuple1=(11,[22,33],44,55)
tuple1[1][0]=222
print("tuple1: ",tuple1)