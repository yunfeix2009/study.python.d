def bubble_sort(arry):
    n = len(arry)
    for i in range(n - 1, 0, -1):
        flag = 1
        for j in range(0, i):
            if arry[j] > arry[j + 1]:
                arry[j], arry[j + 1] = arry[j + 1], arry[j]
                flag = 0
        if flag:
            break
    return arry
arry = [5, 4, 5, 7, 9, 3, 2, 3, 4]
print("排序前")
print(arry)
bubble_sort(arry)
print("排序后")
print(arry)