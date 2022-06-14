# 内置函数

# dir()
# super()
# locals() globals()



# dir() 返回属性和方法的列表
# 不带参数时，返回当前范围内属性和方法的列表                
# 带参数时，返回参数的属性、方法列表。
    # 如果参数包含__dir__()，该方法将被调用。
    # 如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
# print(dir()) 
# print(dir([]))#查看列表的方法




# 课堂练习：
# 隐藏的消息:
# 把下面字符串拆成单词,并从第一个单词开始打印每个单词
# s='this if is you not are a reading very this good then way youto have hide done a it message wrong'
# 尝试用dir和help来找出需要用什么函数，怎么用这个函数





# super()
# 用于调用父类(超类)
# 指定类名时，调用指定类后面的类的方法
# 不写参数时，调用当前类后面的类的方法

class A:
    def add(self,x):
        y = x+1
        print(y)
class B(A):
    def add(self,x):
        super().add(x)
# b=B()
# b.add(2)


# 课堂练习：
# 继承衣钵
# 尝试写一个儿子类，儿子类要继承父亲类和母亲类的属性和函数，
# 但现在要求身高必须要继承父亲类的？






# locals() 以字典类型返回当前位置的全部局部变量
# globals()以字典类型返回当前位置的全部全局变量
#           局部变量       全局变量
# 定义：    函数内定义     函数外定义 
# 作用域：  函数内有效      全局有效


# def runoob(arg):    # 两个局部变量：arg、z
#     z = 1
#     print (locals())
# runoob(4)

# a='runoob'
# print(globals())





# 课堂练习：
# 以下代码输出什么
def foo(arg,a):
    x=100
    y="hello python!"
    for i in range(10):
        j = 1
        k = i
    print(locals())
foo(1,2)


















