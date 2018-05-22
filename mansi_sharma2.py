# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:16:19 2018

@author: mansi sharma
"""

str1=raw_input("enter string")
print str1
dict1={}

for i in str1:
    r=str1.count(i)
    dict1[i]=r
    
print dict1    
    