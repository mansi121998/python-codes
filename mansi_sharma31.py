import re 
lis1=[]
chk_email = []
while True:
   str1=raw_input("enter email")
   
   if not str1:
       break 
   chk_email.append(str1)
   
   
for i in chk_email:
    regex=re.compile(r'[a-z0-9-_]+@[a-z0-9]+\.[a-z]{2,4}$')
    response=regex.match(i)
    
    if response :
        lis1.append(i)



print lis1