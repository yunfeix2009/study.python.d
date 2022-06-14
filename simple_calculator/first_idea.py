print('这是一个简易的计算器')
print('操作符只有“+”，“-”，“*”，“/”')

while True:
    try:
        num1=int(input('请输入要操作的第一个数'))
        print(' ')
        break
    except:
        print('输入不正确。')
        print('请正确输入。')

while True:
    try:
        num2=int(input('请输入要操作的第二个数'))
        break
    except:
        print('输入不正确。')
        print('请正确输入。')

while True:
    operator = input('请输入要操作符')
    print(' ')
    if operator=='+':
        print('结果是',num1+num2)
        break
    elif operator=='-':
        print('结果是', num1-num2)
        break
    elif operator == '*':
        print('结果是', num1 * num2)
        break
    elif operator == '/':
        print('结果是', num1 / num2)
        break
    else:
        print('输入不正确。')
        print('请正确输入。')