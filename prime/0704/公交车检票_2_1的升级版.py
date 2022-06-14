print('一个人2元')
while True:
    try:
        monny=float(input('请输入公交卡余额。（元）'))
        break
    except:
        print('输入不正确。')
        print('请正确输入。')
while True:
    try:
        people=int(input('请输入有几人要上车。（人）'))
        if people <=0:
            print('输入不正确。')
            print('请正确输入。')
            while True:
                try:
                    people = float(input('请输入有几人要上车。（人）'))
                    break
                    while True:
                        try:
                            monny = float(input('请输入有几人要上车。（人）'))


                            break
                        except:
                            print('输入不正确。')
                            print('请正确输入。')
                    break
                except:
                    print('输入不正确。')
                    print('请正确输入。')
        break
    except:
        print('输入不正确。')
        print('请正确输入。')
if monny>=2*people :
    while True:
        try:
            howMeny = float(input('请输入公交车有几座。（座）'))
            if howMeny <=0:
                print('输入不正确。')
                print('请正确输入。')
                while True:
                    try:
                        howMenyPeople = float(input('请输入公交车上有几个座。（座）'))
                        break
                    except:
                        print('输入不正确。')
                        print('请正确输入。')
                break
            break
        except:
            print('输入不正确。')
            print('请正确输入。')
    while True:
        try:
            howMenyPeople = float(input('请输入公交车上有几个人。（人）'))
            if howMeny<howMenyPeople:
                print('输入不正确。')
                print('请正确输入。')
                while True:
                    try:
                        howMenyPeople = float(input('请输入公交车上有几个人。（人）'))

                        break
                    except:
                        print('输入不正确。')
                        print('请正确输入。')
                break
            if howMenyPeople<=0:
                print('输入不正确。')
                print('请正确输入。')
                while True:
                    try:
                        howMenyPeople = float(input('请输入公交车上有几个人。（人）'))

                        break
                    except:
                        print('输入不正确。')
                        print('请正确输入。')
                break
        except:
            print('输入不正确。')
            print('请正确输入。')
            print(' ')
        if howMeny-people>=howMenyPeople:
            print(' ')
            print('恭喜你，可乘坐。')
            break
        else:
            print(' ')
            print('坐满了，不能乘坐。')
            break



else:
    print(' ')
    print('公交卡余额不足。')
    print('不能乘坐。')