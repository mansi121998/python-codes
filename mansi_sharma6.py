# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:27:50 2018

@author: mansi sharma
"""

lis1=input("enter nos")
print lis1


def add(a): 
    c=sum(a)
    print("sum=",c)

def mul(a):
    reduce((lambda x,y:x*y),a)
    
def lar(a):
    c=max(a)
    print ("largest=",c)
    
    
def smal(a):
    c=min(a)
    print("smallest=",c)
    
def sorting(a):
    lis2=sorted(a)
    print("sorted=",lis2)
    
    
def remove_duplicates(a):
    lis2=list(set(a))
    print("without duplicates=",lis2)
    
    
    
def prints():
    add(lis1)
    mul(lis1)
    lar(lis1)
    smal(lis1)
    sorting(lis1)
    remove_duplicates(lis1)
    
    
prints()    
    
    
    
    
    
    
         
    
     
    
    

