while True:
    T=input('有票么（有、没有）')
    if T=='有' or T=='没有':
        if T=='有':
            try:
                S=float(input('刀子的长度'))
            except:
                S = float(input('请重新输入（刀子的长度）'))
                if S<10:
                    print('没有问题')
                    break
                else:
                    print('就地枪毙')
                    print('突突突')
                    print('突突突')
                    print('突突突')
                    print('突突突')
                    print('突突突')
                    print('突突突')
                    print('突突突')
            else :
                print('携带违禁品')
                print('就地枪毙')
                print('突突突')
                print('突突突')
                print('突突突')
                print('突突突')
                print('突突突')
                print('突突突')
                print('突突突')
                break

        else:
            print('请购票')
            break
    else:
        print('请正确输入')
