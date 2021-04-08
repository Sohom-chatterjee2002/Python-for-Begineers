# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:37:33 2020

@author: Sohom Chatterjee_CSE1_T25
"""

#Merge following two Python dictionaries into one dict1 = {'Ten': 10, 'Twenty': 20,'Thirty': 30} dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1={'Ten':10,'Twenty':20,'Thirty':30}
dict2={'Thirty':30,'Fourty':40,'Fifty':50}
dict3={**dict1,**dict2}
print(dict3)