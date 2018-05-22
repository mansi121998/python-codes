# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:27:58 2018

@author: mansi sharma
"""

str1=raw_input("enter string")
print str1
d=0
a=0
for i in str1:
    if i.isalpha():
        a=a+1
    if i.isdigit():
         d=d+1
         

print ("d=",d)
print ("a=",a)

        
      