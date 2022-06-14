# 内置函数
# isinstance()
# callable()
# help() 
# id()
# vars()





# isinstance()判断一个对象是否是这个类的实例（是否是这个数据类型）
# isinstance(对象, 类型)
# 返回值:bool

# print(isinstance(2,int))
# print(isinstance(2,str))
# print(isinstance("2",str))

# 第二个参数可以是类型的元组,属于元组中的一个则返回True
# print(isinstance(2,(str,int,list)))
# print(isinstance("2",(str,int,list)))
# print(isinstance((1,2),(str,int,list)))
# print(isinstance((1),(str,int,list)))
# print(isinstance((1,),(str,int,list)))




# 课堂练习：
# 判断False是不是bool类型,是不是int类型



# print(isinstance(False,bool))
# print(isinstance(False,int))

# bool类型是int的子类

# 其他类型参与逻辑运算:
# False,0,空字符串""(空列表[],空字典{},空元组(),None)都相当于False
# 总结:空的相当于False,不空的都相当于True
# print(not 0)
# print(not 4)
# print(not "1111")
# print(not "")
# print(not " ")
# print(True and 0)

# bool类型可以和数字相加减(True和False值分别是1和0)
# print(True + 1)
# print(False + 1)

# callable() 检查对象是否可调用
# callable(object)
# 返回值：可调用返回True,否则返回False。
# 返回True,仍可能调用失败;返回False,一定调用失败
# 对于函数、lambda函数式、类以及实现了__call__方法的类的实例, 都返回True

# print(callable(0))
# print(callable("runoob"))

# 函数
# def add(a,b):
#     return a+b
# print(callable(add))

# 类
# class A:
#     pass
# print(callable(A))

# 类的实例
# class A:#未实现__call__方法
#     pass
# a = A()
# print(callable(a))

# class B:#实现了__call__方法
#     def __call__(self):
#         return 0
# b = B()
# print(callable(b))



# help() 查看帮助
# help(object)
import time
# print(help("time"))#查看time模块的帮助
# print(help("str"))#查看str数据类型的帮助
# a = [1,2,3]
# print(help(a))#查看列表 list 帮助信息
# a = [1,2,3]
# print(help(a.append))#显示list的append方法的帮助





# id()
# 获取对象的内存地址
# a = "runoob"
# print(id(a))
#
# b=1
# print(id(b))




# vars()
# 返回对象的属性和属性值组成的字典

# class People:
#     a = 1
#     def __init__(self,age,name):
#         self.age=age
#         self.name=name
# p = People(15,"xiaoming")
# print(vars(p))
#
# class Runoob:
#     a = 1
# print(vars(Runoob))


# 如果没有参数，打印当前调用位置的属性和属性值
# print(vars())


# 课堂练习：
# a=4
# b=a
# c=4
# a,b,c的id相同吗？


# a=4
# b=a
# c=4
# print(id(a),id(b),id(c))





# 课后作业
# a = 447
# b = 447
# # 请写程序验证a,b的id值相等吗？
# print(id(a))
# print(id(b))
