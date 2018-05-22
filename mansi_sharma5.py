# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:04:11 2018

@author: mansi sharma
"""

a=input("enter no")
print a
l=len(a)
a=list(a)
if l==0:
    print ("0")
while 13 in a:
    index=a.index(13)
    a.remove(13)
    if index<len(a)-1:
        temp=a[index +1]
        a.remove(temp)
   
print sum(a)     
   
   
        
    
     
     
        

        