import re 
lis1=[]
chk_no = []
while True:
   str1=raw_input("enter credit card no  ")
   
   if not str1:
       break 
   chk_no.append(str1)
   
   
for i in chk_no:
    regex=re.compile(r'[4-6]{1}[0-9]{3}-[0-9]{4}-[0-9]{4}-][0-9]{4}')
    response=regex.match(i)
    
    if response:
        print ("valid")
    else:
        print("not valid")
   