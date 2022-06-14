print('这是一个简易的计算器')
print('操作符只有“+”，“-”，“*”，“/”')

while True:
    flag = False
    while True:
        try:
            num1=int(input('请输入要操作的第一个数'))
            print(' ')
            break
        except:
            print('输入不正确。')
            print('请正确输入。')
            print(' ')

    while True:
        if flag:
            break
        try:
            num2=int(input('请输入要操作的第二个数'))
            print(' ')
            break
        except:
            print('输入不正确。')
            print('请正确输入。')
            print(' ')

    while True:
        if flag :
            break

        operator = input('请输入要操作符')
        print(' ')
        
        if operator=='+':
            print('结果是',num1+num2)
            while True:
                still = input('是否继续 （是，否）：')
                print(' ')
                list_temp = ['是', '否']
                if still in list_temp:
                    if still == '是':
                        flag=True
                        break
                    if still == '否':
                        exit()

        elif operator=='-':
            print('结果是', num1-num2)
            while True:
                still = input('是否继续 （是，否）：')
                print(' ')
                list_temp = ['是', '否']
                if still in list_temp:
                    if still == '是':
                        flag=True
                        break
                    if still == '否':
                        exit()

        elif operator == '*':
            print('结果是', num1 * num2)
            print(' ')
            while True:
                still = input('是否继续 （是，否）：')
                print(' ')
                list_temp = ['是', '否']
                if still in list_temp:
                    if still == '是':
                        flag=True
                        break
                    if still == '否':
                        exit()

        elif operator == '/':
            try:
                print('结果是', num1 / num2)
            except:
                print(' ')
                print('不能把0作为除数！')
                print('默认从新开始。')
                continue
            while True:
                still = input('是否继续 （是，否）：')
                print(' ')
                list_temp = ['是', '否']
                if still in list_temp:
                    if still == '是':
                        flag=True
                        break
                    if still == '否':
                        exit()

                else:
                    print('输入不正确。')
                    print('请正确输入。')
                    print(' ')

        else:
            print('输入不正确。')
            print('请正确输入。')
            print(' ')