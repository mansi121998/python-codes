str1=raw_input("enter string")

def check(str2):
    a="abcdefghijklmnopqrstuvwxyz"
    
    for i in a:
        
        if i not in str2:
            return False
                
    return True
    
check(str1)          

if check is True: print ("pangram")
else: print("not pangram")
      