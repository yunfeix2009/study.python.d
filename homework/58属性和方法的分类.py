# 属性的分类：类属性，实例属性

# 方法的分类：类方法，实例方法，静态方法







# 属性的分类：类属性和实例属性

#              类属性                 实例属性(对象属性)            
# 定义：定义在类里面，__init__方法外   
# 所有：类所有，所有实例共享          各个实例所有，互不干扰
# 访问：通过类和实例对象访问          只能通过实例对象访问
# 修改：通过类或类方法修改
#       不能通过实例修改 
            
            
# 类属性
# class People:
#     name = 'Tom' #类属性

# 类属性的访问
# p1 = People()
# print(p1.name) # 通过实例对象访问
# p2 = People()
# print(p2.name) # 通过实例对象访问

# print(People.name) # 通过类访问


# 实例属性(对象属性)
class People(object):
    address = '山东' # 类属性
    def __init__(self):
        self.name = 'xiaowang' # 实例属性
        self.age = 20 # 实例属性

p=People()
# 类属性的访问
# print(p.address)
# print(People.address)

# 实例属性的访问
# p.age=12#实例属性
# print(p.name)
# print(p.age)
# print(People.name)
# print(People.age)


# 总结:
# 类属性可以通过类和实例对象访问
# 实例属性只能通过实例对象访问




# 类属性的修改
class People:
    country='china'#类属性

# # 通过类修改类属性
# print("修改前的类属性",People.country)
# People.country="japan"
# print("修改后的类属性",People.country)

# 通过实例对象修改类属性
p=People()
# print("修改前的类属性",p.country)
# p.country='Japan'
# print(p.country)
# print("修改后的类属性",People.country)

# 当删除实例属性后，再使用相同的名称，访问到的将是类属性。
# del p.country #删除实例属性
# print("删除后的属性",p.country)


# 注意：
# 1用实例对象修改类属性，不会影响到类属性
# 会产生一个同名的实例属性，这种方式修改的其实是实例属性

# 2实例属性和类属性不要使用相同的名字
# 因为同名的实例属性的优先级高于类属性

# 3技巧：操作类属性使用类，操作实例属性使用实例对象




# 课堂练习
# 下面的程序将得到什么结果？
class MixData:
    data = 'spam'# 类属性
    def __init__(self, value):
        self.data = value # 实例属性
    def disPlay(self):
        print(self.data, MixData.data)

if __name__ == '__main__':#程序运行的入口
    x = MixData(1024)
    x.disPlay()

# __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 
# 这句话的意思就是，当模块被直接运行时，以下代码块将被运行
# 当模块是被导入时，代码块不被运行







# 方法的分类：类方法，实例方法，静态方法
#            类方法            实例方法             静态方法
# 修饰器：   @classmethod            无           @staticmethod 
# 第一个参数：类对象cls        实例对象self         无要求
# 调用:  通过类和实例对象      通过实例对象       通过类和实例对象


# 静态方法的作用：
# 用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系
# 静态方法中不会涉及到类中的属性和方法的操作
# 可以理解为，静态方法是个独立的、单纯的函数


# 类方法
# class People:
#     country='china'#类属性
#     @classmethod
#     def get_country(cls):#类方法用@classmethod来修饰
#         return cls.country#这里表示的是类属性
# p=People()
# print(p.get_country())#用实例对象调用
# print(People.get_country())#通过类本身调用


# 类方法的一个用途：修改类属性
# class People:
#     country='china'
#     @classmethod
#     def get_country(cls):
#         return cls.country
#     @classmethod
#     def set_country(cls,country):
#         cls.country=country

# p=People()
# print("修改前的类属性：",p.get_country())
# print("修改前的类属性：",People.get_country())
# p.set_country("japan")
# print("修改后的类属性：",p.get_country())
# print("修改后的类属性：",People.get_country())



# 静态方法
# class People:
#     country='china'
#     @staticmethod  
#     def get_country():#静态方法
#         return People.country

# p=People()
# print(p.get_country())#通过对象访问静态方法
# print(People.get_country())#通过类访问静态方法


