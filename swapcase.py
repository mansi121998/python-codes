
str=raw_input("enter string ")

def swap_case(s):
 t=[]   
 for i in s:
    if i.islower() is True:
        t.append(i.upper())
    if i.isupper() is True:
         t.append(i.lower())
         
    
 return "".join(t)
     
swap_case(str)