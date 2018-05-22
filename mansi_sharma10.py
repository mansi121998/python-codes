

str1=raw_input("enter string")




def tanslate(str2):
    st3=''
    lis1=['a','e','i','o','u',' ']
    for i in str2:
        if i not in lis1:
           st3=st3+i+"o"+i 
        else:
            st3=st3+i
    return st3        

tanslate(str1)