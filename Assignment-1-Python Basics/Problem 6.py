# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:55:43 2020

@author: Sohom Chatterjee_CSE1_T25
"""

# Display two substring by separated space.
def convert(lst):
    return str(lst).translate(None, '[],\'')
lst=['computer','science','engineering']
print(convert(lst))