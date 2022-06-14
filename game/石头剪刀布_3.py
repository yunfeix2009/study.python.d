def play() :
    import time
    import random
    list = ['石头','剪子','布']
    print('你好，这里是一个【石头剪子布】游戏')
    player = input('请输入【石头，剪子，布】要出什么:  ')
    print('石头！~')
    time.sleep(1)
    print('剪子！~')
    time.sleep(1)
    print('布！~')
    time.sleep(1)
    computer = list[random.randint(0,2)]
    dic={
        '石头-剪子':"赢",'剪子-布':"赢",'布-石头':"赢",'石头-石头':"和",'剪子-剪子':"和",'布-布':"和",'布-剪子':"输",'石头-布':"输",'剪子-石头':"输"
    }
    key = player + '-' + computer
    try :
        print(key,dic[key])
    except:
        print('请正确输入')
        play() # 递归调用函数
play()