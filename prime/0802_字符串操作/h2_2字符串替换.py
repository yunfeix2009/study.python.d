def str_reversal (str,str_1,str_2):
    str=str[::-1]
    str_1=str_1[::-1]
    str_2=str_2[::-1]
    str = str.replace(str_1,str_2,1)
    str=str[::-1]
    print(str)
str_reversal('stevenisadog','dog','student')