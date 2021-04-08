# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:47:30 2020

@author: Sohom Chatterjee_CSE1_T25
"""

#Get the key corresponding to the minimum value from the following dictionary
#sampleDict = { 'Physics': 82, 'Math': 65, 'history': 75}
sampleDict = { 'Physics': 82, 'Math': 65, 'history': 75}
print(min(sampleDict,key=sampleDict.get))