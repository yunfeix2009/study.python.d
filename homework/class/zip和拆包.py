# zip() 打包
# 解包
# zip对象转字典



# zip() 打包,对应的转元组
# 意义：节约内存
# 参数：一个或多个可循环对象
# 返回值：zip对象


# 对应的转元组
# print((zip([1,2,3],[4,5,6])))
# a = zip([1,2,3],[4,5,6])
# print(type(a))
# 可使用list()转换成列表来输出
# print(list(zip([1,2,3],[4,5,6])))
# print(list(zip([1,2,3],[4,5,6],[7,8,9])))

# a,b,c = zip([1,2,3],[4,5,6])
# a,b,c = (1, 4) ,(2, 5) ,(3, 6)
# print(a,b,c)

# print(list(zip("123","456")))
# print(list(zip((1,2,3),[4,5,6])))
# print(list(zip((1,2,3),{4:5,5:6,6:7})))#只和字典的键对应


# 如果参数的长度不一致，结果的长度与最短的对象相同
# print(list(zip([1,2,3],[4,5,6,7])))

# print(list(zip([1,2,3])))



# 解包
# 将一个可循环对象解包为多个对象

# 用*号可以
# print((1,2,3,4))
# print(*(1,2,3,4))

# a,b,c,d = (1,2,3,4)
# print(a,b,c,d)

# print(*range(5))

# a = zip([1,2,3],[4,5,6])
# print(*a)

# print(*zip([1,2,3],[4,5,6,7]))

# a1,a2 = zip(*zip([1,2,3],[4,5,6,7]))
# print(a1)
# print(a1,a2)



# 利用zip可以创建字典(很常用)
# a1,a2,a3 = zip([1,2,3],[4,5,6,7])
# print(a1,a2,a3)


# 把zip对象转成字典
# print(dict(zip([1,2,3],[4,5,6,7])))
# print(dict(zip("123",[4,5,6,7])))




# 课后作业1
# 将下面这两个列表生成字典:{'a':1,'b':2,'c':3}
# keys = ['a','b','c']
# values = [1, 2, 3]
# print(dict(zip(keys,values)))


# 课后作业2
# 学生考试成绩要和姓名对应起来，怎么更快的分配呢？
tb=[['小明','小红','小白'],[90,80,70]]
keys=tb[0]
values=tb[1]
# keys,values = tb
print(keys,values)

# print(dict(zip(keys,values)))
# print(dict(zip(* tb)))



