import re
str1=raw_input("enter the details ")
         
print str1
regex = re.compile(r'[0-9+-.]+\.[0-9]+')
response=regex.match(str1)

if response :
    print ("True")
else:
    print("False")   
    

                  
    
        