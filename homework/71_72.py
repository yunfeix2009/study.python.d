import re,os
# result=re.search('0([1-9][0-9]{0,2})$',"100203")
# print(result.groups())
#
# result_f2=re.search('0([1-9][0-9]*)','100203')
# print(result_f2.groups())


for line in open("file.txt",'r'):
    if not line==line.rstrip()+'\n':
        continue
    try:
        if re.match('([0-9]{3}-|\(\d{3}\))[0-9]{4}-[0-9]{3}', line.rstrip()):
            print(re.match('([0-9]{3}-|\(\d{3}\))[0-9]{4}-[0-9]{3}', line.rstrip()))
    except:
        pass