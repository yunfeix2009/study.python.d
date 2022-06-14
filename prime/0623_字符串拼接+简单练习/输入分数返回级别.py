num=int(input('请输入您的分数(0至100)'))
if num>100 or num<0:
    print('请输入您的正确分数')
elif num<60:
    print('不及格')
elif num==100:
    print('满分')
elif num>80:
    print('优秀')
else:
    print('良好')