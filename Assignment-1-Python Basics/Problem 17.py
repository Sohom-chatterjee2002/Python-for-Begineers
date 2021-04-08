# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:43:59 2020

@author: Sohom Chatterjee_CSE1_T25
"""

#. Rename key city to location in the following dictionary
#sampleDict = { "name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
sampleDict = { "name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
sampleDict['location']=sampleDict.pop('city')
print(sampleDict)