# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:16:15 2018

@author: mansi sharma
"""

         

def brick(lst):
    s,b,g = lst
    if g%5 > s:
        return False
    if s+b*5 >= g:
        return True
    else:
        return False

lis1=input("enter the nos")
print brick(lis1)
 
    

        
              
        
       
        

    
    
        
        
    
        
        
        
    
        
        
        
        

        