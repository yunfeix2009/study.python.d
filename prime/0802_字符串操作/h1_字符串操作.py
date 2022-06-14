str=input('输入一个字符串。')
isalpha=0
isdigit=0
isspace=0
other=0
for i in str:
    if i.isalpha():
        isalpha+=1
    elif i.isdigit():
        isdigit+=1
    elif i.isspace():
        isspace+=1
    else:
        other+=1
print('字母个数= %d,数字个数= %d,空格个数= %d,个数其他字符的= %d'%(isalpha,isdigit,isspace,other))