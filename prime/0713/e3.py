# 输出三科成绩的等级
temp=0
while True:
    scar=int(input('请输入成绩。'))
    if scar>=90:
        print('优秀')
    elif scar>=70:
        print('良好')
    elif scar>=60:
        print('及格')
    else:
        print('不及格')
    temp+=1
    if temp==3:
        break
