str1=raw_input ("enter nos ")
lis1=str1.split(' ')

list2 = []
list3 = []

for i in lis1:
     if all([i==i[::-1]]):
        list2.append(True)
     else :
        list2.append(False)
        
for item in lis1:
    if int(item) > 0:
        list3.append(True)
    else:
        list3.append(False)
        
all([ any(list2), all(list3)])