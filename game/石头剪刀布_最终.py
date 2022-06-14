from time import *
from random import *
def play():
    score=0
    print('你好，这里是一个【石头剪子布】游戏')
    print('赢-加2分，和-加1分，输-不加分')
    still = '是'
    while True:
        list_still=['是','否']
        if still in list_still:
            if still=='否':
                print('恭喜你，共得分：',score)
                return
            list = ['石头','剪子','布']
            print('')
            player = input('请输入【石头，剪子，布】要出什么:  \n')
            if player in list:
                print('石头！~')
                sleep(1)
                print('剪子！~')
                sleep(1)
                print('布！~')
                sleep(1)
                print(' ')
                computer=randint(0,2)
                if computer==0 and player=='布' or computer==1 and player=='石头' or computer==2 and player=='剪子':
                    print('赢')
                    score+=2
                if computer==2 and player=='布' or computer==0 and player=='石头' or computer==1 and player=='剪子':
                    print('和')
                    score+=1
                if computer==1 and player=='布' or computer==2 and player=='石头' or computer==0 and player=='剪子':
                    print('输')
                print(' ')
                print('目前得分：',score)
                print(' ')
                still = input('继续玩么？（是，否）：\n')
            else:
                print('输入不正确！\n')
        else:
            still = input('请正确输入:（是，否）：\n')

play()
