from collections import OrderedDict

d=OrderedDict()
while True:
    str1=raw_input()
    if not str1:
        break
    lis1=str1.split(" ")
    
    value=lis1[-1]
    key=' '.join(lis1[0:-1])
    if key in d:
        d[key]= d[key]+ int(value)
        
    else:
         d[key]=int (value)
         
for key,value in d.items():
     print key,value
         
        

