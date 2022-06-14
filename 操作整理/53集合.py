# 集合
# 1集合的创建(两种方式)
# 2集合的特点(三个特点)
# 3对集合元素的操作(添加，删除)
# 4两个集合间的运算(交，并，差，对称差)
# 5set,tuple,list之间相互转换
# 6frozenset()







#1 创建集合：
# 方式1：myset = {value1,value02,...}
# myset = {1,2,3,4,5}
# print(myset)

# 方式2：set()
# myset = set([0,1,2,3,0,1,2,3])
# print(type(myset))
# myset = set("hello")
# print(myset)
# myset = set((1,2,3,4,5))
# print(myset)
# mytest =set({"111":11,"2":2}) 
# print(mytest)

# 注：创建空集合必须用set(),而不是{}，因为{}是用来创建一个空字典
# mytest ={}
# print(type(mytest))

# mytest =(4)
# print(type(mytest))


# 2 集合的特点：
# 无序(没有先后之分，无法通过索引获取)
# 不重复(应用：去重复)
# 不可变（不可修改，可删除）
# myset = {1,32,3,41,5}
# print(myset)
# print(myset[1])



# myset = {1,32,3,41,5,32,3}
# print(myset)




# 3对集合里元素的操作(增，刪，改，查)
# 增：add()添加一个元素
# myset = {1,2,3,4,5}
# myset.add(6)
# print(myset)


# 刪：remove()
# myset = {1,2,3,4,5}
# myset.remove(3)
# print(myset)


# 改：不可修改
# 查：不可查询



# 4两个集合间的运算(交，并，差，对称差)
# 交集(&)
# a和b中都包含的元素
# a = set('abcde')
# b = set('acm')
# c = a & b
# print(c)


# 并集(|)
# a或b中包含的所有元素
# a = set('abcde')
# b = set('acm')
# c = a | b
# print(c)



# 差集（-）
# a - b #在a中而不在b中的元素
# a = set('abcde')
# b = set('acm')
# c = a - b
# c = b - a
# print(c)


# 对称差集（^）
# a ^ b 
# 不同时在a和b中的元素
# 只属于其中一个集合，而不属于另一个集合的元素
# (a | b) - (a & b)
# a = set('abcde')
# b = set('acm')
# print(a ^ b)
# print((a | b) - (a & b))


# 5 set,tuple,list之间相互转换
# set() tuple() list()

# a_set = set('abcde')
# a_list = list(a_set)
# print(type(a_list))

# a_set = set('abcde')
# a_tuple=tuple(a_set)
# print(type(a_tuple))

# a_list = [1,2,3,4]
# a_set = set(a_list)
# print(type(a_set))

# a_list = [1,2,3,4]
# a_tuple = tuple(a_list)
# print(type(a_tuple))

# a_tuple=(1,2,3,4)
# a_list = list(a_tuple)
# print(type(a_list))

# a_tuple=(1,2,3,4)
# a_set = set(a_tuple)
# print(type(a_set))

# ​frozenset() 创建一个不可变的集合(frozen冷冻的)
# 参数：可循环对象
# 返回值：frozenset对象
#        如果无参数，默认返回空的frozenset对象

# print(frozenset(range(10)))
# print(frozenset([1,2,3,4]))
# print(frozenset("hello"))
# print(frozenset())



# 课堂练习
# 将以下两个列表合并并去重,结果仍然是列表
my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = [1, 2, 3, 4, 5, 10, 7, 8, 9]
print(list(set(my_list1)|set(my_list2)))


# 课后作业
# 使用set集合获取两个列表中的相同元素。
l1 = {11,22,33}
l2 = {22,33,44}
print(list(l1&l2))