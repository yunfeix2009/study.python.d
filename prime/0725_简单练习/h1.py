# 模拟登录
while True:
    name=input('输入用户名（小于等于三字）(设定)。\n')
    if len(name)<=3 and len(name)>=0:
        break
    else:
        print('输入不正确。')
        print('请正确输入。')
while True:
    try:
        password=input('输入密码（六位数字）(设定)。\n')
        if len(password) == 6:
            break
        else:
            print('输入不正确。')
            print('请正确输入。')
    except:
        print('输入不正确。')
        print('请正确输入。')
while True:
    judge=input('是否登录（否即为退出程序）。\n')
    if judge=='是':
        for i in range(1,4):
            while True:
                name_2 = input('输入用户名。\n')
                if name_2==name:
                    for i in range(1,4):
                        password_2 = input('输入密码。\n')
                        if password_2==password:
                            exit()
                        else:
                            print('输入不正确。')
                            print('请正确输入。')

                else:
                    print('输入不正确。')
                    print('请正确输入。')

    elif name=='否':
        exit()
    else:
        print('输入不正确。')
        print('请正确输入。')
