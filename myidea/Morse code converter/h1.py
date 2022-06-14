while True:

    wich=input('如果需要摩斯密码转换成英语请输入是，逆转请输入否。')
    if wich=='是' or '否':
        break
    else:
        print('输入不正确。')
        print('请输入是或否。')
if wich=='是':
    while True:
        str = input('请输入摩斯密码')
        for i in str:
            if i== ' ' or '_' or '.':
                break
        else:
            print('输入不正确。')
            print('请输入：空格,英语句号,下划线。')
str_list=str.split()
