while True:
    str=input('输入一个字符串。\n')
    if not str=='':
        break
    else:
        print('输入不正确。')
        print('不能输入空字符串。')
while True:
    str_1=input('输入要替换的子字符串。\n')
    if not str_1=='' and str_1 in str:
        break
    elif str_1=='' :
        print('输入不正确。')
        print('不能输入空字符串。')
    else:
        print('输入不正确。')
        print('子串必须在原字符串内字符串。')
while True:
    str_2=input('输入要替换成的字符串。\n')
    if not str=='':
        break
    else:
        print('输入不正确。')
        print('不能输入空字符串。')
str=str[::-1]
str_1=str_1[::-1]
str_2=str_2[::-1]
str = str.replace(str_1,str_2,1)
str=str[::-1]
print(str)
