# 输出一个空心三角形字符画
for i in range(7):
    for j in range(i):
        if i >= 3 and i <= 5:
            if j == 0 or j == i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print("*", end=" ")

    print()