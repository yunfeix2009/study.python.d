# 课堂练习：
# 考试后,有的学生成绩无效(如0分和None)
# 无效成绩会影响班里的平均成绩，需要去除
# 有成绩列表score
# score=[67,89,0,None,100,45,91,99,43]
# 要求：
# 1判断成绩列表是否有需要去除的
# 2如果有,则去除无效的成绩
# if all(score):
#     print('没有')
# else:
#     while True:
#         for i in score:
#             if i==0 or i==None:
#                 score.remove(i)
#         if not 0 in score and not None in score:
#                 break
#     print(score)
# i=len(score)-1
# while i>=0:
#     if not(score[i]==0 or score[i]==None):
#         print(score[i])
#     i=i-1
# any()
# 判断可迭代对象中是否有元素等价于True
# 如果是返回True,否则返回False

# print(any(["a","b","c"]))
# print(any(["a","b","c",""]))
# print(any(["a",None,0,""]))
# print(any([False,None,0,""]))
# print(any([False,None,0," "]))


# any()等价于：
# def myany(iterable):
#     for x in iterable:
#         if x:
#             return True
#     return False


# 小练习：
# print(any([0,2,4,6,8,""]))
# print(any([0,2,4,6,8]))
# print(all([False,None,0,[]]))
# print(any([False,None,0,""]))


# 课堂练习：
# 1.判断[12,-80,"a", 0, None]中是否全部为True
# 2.输出上面列表中相当于True的值


# 课后作业
# 写一个函数,找出学生的有效信息,并输出
# 提示：
# 1先判断学生信息列表是否有有效的信息,
# 2如果有,则输出有效的信息
# students=['王三','李四','赵五','唐二',None]

# 写一个函数,找出学生的有效信息,并输出
# 提示：
# 1先判断学生信息列表是否有有效的信息
# 2如果有,则输出有效的信息
# students=['王三','李四','赵五','唐二',None]
# if any(students):
# #     print('有')
# # for i in students:
# #     if i:
# #         print(i)

# for i in students:
#     print(i == students[students.index(i)])
# 1 定义第一个函数oneLine()：打印一条横线"------------------"
# 2 定义第二个函数multiLine(n)：参数为n,打印n条横线（调用第一个函数）
# 如：n =5
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------

# def oneLine():
#     print('-------------------------------')
# def manyLine(n):
#     for i in range(n):
#         oneLine()
# manyLine(5)

# 设计一个函数：求三个数的平均值
# 要求: 使用函数的嵌套,在求三个数的平均值的函数里调用求三个数的和的函数
def sum(a,b,c):
    return a+b+c
def mean(a,b,c):
    print(sum(a,b,c)/3)
mean(1,2,3)