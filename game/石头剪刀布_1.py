import random
print('这里是一个剪刀石头布的小游戏')
temp=input('请输入要出什么')
temp2=random.randint(0,2)
#
if temp=='剪刀':
    if temp2==0:
        print('我们输了')
    if temp2==1:
        print('我们平局')
    if temp2==2:
        print('我们赢了')
if temp=='布':
    if temp2==0:
        print('我们输了')
    if temp2==2:
        print('我们平局')
    if temp2==1:
        print('我们赢了')
if temp=='石头':
    if temp2==2:
        print('我们输了')
    if temp2==0:
        print('我们平局')
    if temp2==1:
        print('我们赢了')