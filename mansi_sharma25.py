lis1=[]


while True:
        str1=raw_input("enter the details ")
        if not str1:
             break 
        tup1=str1.split(",")
        lis1.append((tup1[0],int(tup1[1]),int(tup1[2])))


 
lis1.sort()
print lis1