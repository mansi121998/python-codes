# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:45:34 2018

@author: mansi sharma
"""

a=input("enter string")
print a
b=list(a)
b.sort()
b.pop()

del b[0]
print b
print sum(b)/len(b) 
