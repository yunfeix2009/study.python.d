# 输出一个空心三角形字符画
while True:
    try:
        Number_of_rows=int(input('输入行数。\n'))
        if Number_of_rows>=0:
            break
        else:
            print('输入不正确。')
            print('请正确输入。')
    except:
        print('输入不正确。')
        print('请正确输入。')
for i in range(Number_of_rows+1):
    for j in range(i):
        if i >= 3 and i <= Number_of_rows-1:
            if j == 0 or j == i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print("*", end=" ")

    print()