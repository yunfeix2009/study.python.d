def divide(x, y):
    if y == 0:
        return '分母不能为0, 计算无效'
    else:
        return x / y
judge = True
symbol = {'1': '+', '2': '-', '3': '×', '4': '÷'}
while judge:
    def counter(x, y, num):
        expression = {'1': x + y, '2': x - y, '3': x * y, '4': divide(x, y)}
        if type(expression[num]) == int or type(expression[num]) == float:
            return '{}{}{}={}'.format(x, symbol[num], y, expression[num])
        else:
            return expression[num]
    print('选择运算：1、相加 2、相减 3、相乘 4、相除')
    chose = input('请输入你的选择（1/2/3/4）：')
    num1 = int(input('请输入第一个数字：'))
    num2 = int(input('请输入第二个数字：'))
    print('计算结果：',counter(num1, num2, chose))
    print('是否离开程序：是（Y） 否（N）')
    choice = input('请选择：')
    if choice == 'Y':
        judge = False
print('程序结束！')