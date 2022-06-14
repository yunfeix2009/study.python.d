from time import *
from random import *
def play():
    while True :
        list = ['石头','剪子','布']
        print('你好，这里是一个【石头剪子布】游戏')
        player = input('请输入【石头，剪子，布】要出什么:  ')
        if player in list:
            print('石头！~')
            sleep(1)
            print('剪子！~')
            sleep(1)
            print('布！~')
            sleep(1)
            computer=randint(0,2)
            if computer==0 and player=='布' or computer==1 and player=='石头' or computer==2 and player=='剪子':
                print('赢')
            if computer==2 and player=='布' or computer==0 and player=='石头' or computer==1 and player=='剪子':
                print('和')
            if computer==1 and player=='布' or computer==2 and player=='石头' or computer==0 and player=='剪子':
                print('输')
        else :
            play()
play()
