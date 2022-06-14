print('这是一个简易的计算器')
print('操作符只有“+”，“-”，“*”，“/”')

flag = True

while True:
    if not flag:
        break

    operator = input('请输入要操作符')
    print(' ')

    if operator == '+':
        while True:
            if not flag:
                break
            try:
                num1 = int(input('请输入要操作的第一个加数'))
                print(' ')
                break
            except:
                print('输入不正确。')
                print('请正确输入。')
                print(' ')
        while True:
            if not flag:
                break
            try:
                num2 = int(input('请输入要操作的第二个加数'))
                print(' ')
                break
            except:
                print('输入不正确。')
                print('请正确输入。')
                print(' ')
        print('结果是', num1 + num2)
        while True:
            if not flag:
                break
            still = input('是否继续 （是，否）：')
            print(' ')
            list_temp = ['是', '否']
            if still in list_temp:
                if still == '是':
                    flag = True
                    break
                if still == '否':
                    exit()

    elif operator == '-':
        while True:
            if not flag:
                break
            try:
                num1 = int(input('请输入要操作的被减数'))
                print(' ')
                break
            except:
                print('输入不正确。')
                print('请正确输入。')
                print(' ')

        while True:
            if not flag:
                break
            try:
                num2 = int(input('请输入要操作的减数'))
                print(' ')
                break
            except:
                print('输入不正确。')
                print('请正确输入。')
                print(' ')

        print('结果是', num1 - num2)

        while True:
            if not flag:
                break
            still = input('是否继续 （是，否）：')
            print(' ')
            list_temp = ['是', '否']
            if still in list_temp:
                if still == '是':
                    flag = True
                    break
                if still == '否':
                    exit()

    elif operator == '*':
        while True:
            if not flag:
                break
            try:
                num1 = int(input('请输入第一个乘数'))
                print(' ')
                break
            except:
                print('输入不正确。')
                print('请正确输入。')
                print(' ')

        while True:
            if not flag:
                break
            try:
                num2 = int(input('请输入第二个乘数'))
                print(' ')
                break
            except:
                print('输入不正确。')
                print('请正确输入。')
                print(' ')

        print('结果是', num1 * num2)
        print(' ')

        while True:
            if not flag:
                break
            still = input('是否继续 （是，否）：')
            print(' ')
            list_temp = ['是', '否']
            if still in list_temp:
                if still == '是':
                    flag = True
                    break
                if still == '否':
                    exit()

    elif operator == '/':
        while True:
            if not flag:
                break
            try:
                num1 = int(input('请输入被除数'))
                print(' ')
                break
            except:
                print('输入不正确。')
                print('请正确输入。')
                print(' ')

        while True:
            if not flag:
                break

            try:
                num2 = int(input('请输入除数'))
                print(' ')
                break
            except:
                print('输入不正确。')
                print('请正确输入。')
                print(' ')

        while True:
            if not flag:
                break

            if num2==0:
                print('不能把0作为除数')
                print('默认重新输入')

                while True:
                    if flag == True:
                        break
                    try:
                        num1 = int(input('请输入被除数'))
                        print(' ')
                        break
                    except:
                        print('输入不正确。')
                        print('请正确输入。')
                        print(' ')

                while True:
                    if not flag:
                        break
                    try:
                        num2 = int(input('请输入除数'))
                        print(' ')
                        break
                    except:
                        print('输入不正确。')
                        print('请正确输入。')
                        print(' ')

            else:
                break

        print('结果是', num1 / num2)

        while True:
            still = input('是否继续 （是，否）：')
            print(' ')
            list_temp = ['是', '否']
            if still in list_temp:
                if still == '是':
                    flag = True
                    break
                if still == '否':
                    flag==False
                    print('简易计算器到此结束')

            else:
                print('输入不正确。')
                print('请正确输入。')
                print(' ')

    else:
        print('输入不正确。')
        print('请正确输入。')
        print(' ')