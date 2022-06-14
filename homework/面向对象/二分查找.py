# 算法基础之二分查找




# mylist=[1,2,3,4,5,6,7,8,9,10]
# 如果想从列表里找到8这个元素的索引,该怎么做
# 以前的做法
# mylist=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(mylist)):
#     if mylist[i] == 8:
#         print(i)
#         break
# 缺点：比较次数多


# 猜数字游戏
# import random
# num = random.randint(1,20)
# while True:
#     a = int(input("请输入一个数字："))
#     if a > num :
#         print("猜大了")
#     elif a < num:
#         print("猜小了")
#     else:
#         print("猜对了")
#         break #结束循环
#
#
#
# 二分查找/折半查找
# 使用条件：有序列表
# [1,2,3,4,5,6,7,8,9,10]
# 优点：比较次数少,查找速度快


# 二分查找思想：
# 1中间索引将列表分成两半(二分)
# 2将中间索引的值与待查找的值比较,更新最小值或最大值来缩小查找范围
    # 如果中间索引的值==待查找的值,则查找成功
    # 如果中间索引的值<待查找值,查找列表的后一子表
    # 如果中间索引的值>待查找值,查找列表的前一子表
# 3重复以上过程
    # 直到找到待查找值,则查找成功,返回对应的索引
    # 或直到子表不存在为止,此时查找不成功,返回-1

# 举例：找8
# [1,2,3,4,5,6,7,8,9,10]



# 实现
# 1 递归实现
# 2 非递归实现



# 递归方式的实现
# def binary_search(mylist, data):#mylist要查找的列表，data待查找元素
#     n = len(mylist)
#     if n < 1:# 递归结束的条件
#         return -1
#     mid = ((n-1) + 0) // 2   #索引的中间值
#     if mylist[mid] > data:
#         return binary_search(mylist[0:mid], data)
#     elif mylist[mid] < data:
#         return mid + binary_search(mylist[mid + 1:], data) + 1
#     else:# mylist[mid] = data
#         return mid
# mylist=[1,2,3,4,5,6,7,8,9,10]
# print(binary_search(mylist,8))



# 非递归方式的实现
# def binary_search(mylist, data):
#     min = 0   # 要查找的列表的最小索引
#     max = len(mylist) - 1 # 要查找的列表的最大索引
#     while min <= max:
#         mid = (max + min) // 2
#         if mylist[mid] > data:
#             max = mid - 1
#         elif mylist[mid] < data:
#             min = mid + 1
#         else:
#             return mid
#     return -1
# mylist=[1,2,3,4,5,6,7,8,9,10]
# print(binary_search(mylist,3))






# 课后作业
# 在一个排序数组中找一个数,返回该数出现的位置,如果不存在,返回-1
# 例如：给出数组
mylist=[1, 2, 2, 4, 5, 5]
# 对于 target = 2, 返回 1 或 2
# 对于 target = 5, 返回 4 或 5
# 对于 target = 6, 返回 -1

def find_2222(list,targent):
    if not targent in list or list==[]:
        return -1
    n=len(list)
    mid=((n-1)+0)//2
    if list[mid]>targent:
        return find_2222(list[0:mid:],targent)
    elif list[mid]<targent:
        return mid+1+find_2222(list[mid+1::], targent)
    else:
        return mid
# index=find_2222(mylist,5)
# print(index)


# def find(list,targent):
#     min=0
#     max=len(list)-1
#     while min<=max:
#         mid=(min+max)//2
#         if list[mid]>targent:
#             max=mid-1
#         elif list[mid]<targent:
#             min=mid+1
#         else:
#             return mid
# index=find(mylist,4)
# print(index)