# 面向对象三大特性：封装、继承、多态

# 封装：


# 多态






# 剧情发展：
# 大猫觉得配方传承下去没问题，
# 但是钱是辛辛苦苦挣得血汗钱，不想传给徒弟。（私有权限）



# 封装：
# 1.模块化
# 比如：把对象的属性和行为看成一个统一的整体，将二者放在一个独立的类中
# 2.私有
# 添加私有权限：在属性名或方法名前加两个下划线__
# 访问：本类内部访问
#       外部对象无法直接访问,子类也无法访问(不会被子类继承)
# 作用：私有的属性和方法,不通过对象调用,更安全


# class Master:#定义Master类
#     def __init__(self):
#         self.kongfu="古法煎饼果子配方"
#     def makecake(self):#实例方法
#         print("按照<%s>制作了一份煎饼果子"%self.kongfu)
# class School:#定义School类
#     def __init__(self):
#         self.kongfu="现代煎饼果子配方"
#     def makecake(self):
#         print("按照<%s>制作了一份煎饼果子"%self.kongfu)
# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu="猫氏煎饼果子配方"
#         self.__money=10000#私有属性,在类内部通过self调用,外部对象不能直接访问
#     def __printinfo(self):#私有方法,在类内部通过self调用,外部对象不能直接访问
#         print(self.kongfu)
#         print(self.__money)
#     def printinfo(self):
#         print(self.kongfu)
#         print(self.__money)
# class PrenticePrentice(Prentice):
#     def printinfo(self):
#         print(self.kongfu)
#         print(self.__money)

# 对象不能直接访问私有属性和方法
# p=Prentice()
# print(p.kongfu)
# print(p.__money)
# p.__printinfo()
# p.printinfo()


# 子类不能继承父类私有属性和方法
# pp=PrenticePrentice()
# pp.printinfo()



# 修改对象属性的两种方式
# 直接修改:对象名.属性名=数据
# 间接修改:对象名.方法名()

# 修改私有属性：
# 无法直接修改(因为不能访问，不是私有属性就可以直接修改)
# 只能间接修改,定义一个非私有方法，在方法内修改私有属性

# class Master:#定义Master类
#     def __init__(self):
#         self.kongfu="古法煎饼果子配方"
# class School:#定义School类
#     def __init__(self):
#         self.kongfu="现代煎饼果子配方"
# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu="猫氏煎饼果子配方"
#         self.__money=10000#私有属性,在类内部通过self调用,外部对象不能直接访问
#     def get_money(self):#通常定义get_×××()方法获取私有属性
#         return self.__money#返回私有属性的值
#     def set_money(self,num):#通常定义set_×××()方法修改私有属性
#         self.__money=num #接收参数，修改私有属性的值
# class PrenticePrentice(Prentice):
#     pass
# damao = Prentice()
# print(damao.get_money())
# damao.set_money(11000)#访问公有方法，修改私有属性
# print(damao.get_money())#访问公有方法，获取私有属性




# 课堂练习:
# 定义一个Message类，它有两个方法：
    # 私有方法：发送短信
    # 公有方法：有一个参数，余额
        # 如果余额大于10000，调用私有方法发短信
        # 否则输出余额不足
# 实例化Message对象，调用公有方法来发短信

class Message:
    def __init__(self,balance):
        self.balance=balance
    def __out_message(self):
        print('我没有发短信')
    def out_message(self):
        if self.balance>10000:
            self.__out_message()
        else:
            print('余额不足，赶紧充钱！')
steven=Message(17549275927381857)
steven.out_message()


# 多态：
# 多态：指一类事物有多种形态
# 作用：
# 用一个函数名调用不同功能的函数
# 增加代码调用的灵活度，让代码更通用


# class Duck:
#     def __init__(self):
#         self.name='duck'
#     def fly(self):
#         print('鸭子飞起来了')
# class Bird:
#     def __init__(self):
#         self.name='bird'
#     def fly(self):
#         print('鸟飞起来了')
# class Func:
#     def fun(self,obj):
#         print(obj.name)
#         obj.fly()
# duck=Duck()
# bird=Bird()
# f=Func()
# f.fun(duck)# 用一个函数名调用不同功能的函数
# f.fun(bird)

# python的多态就是弱化类型
# 重点在于对象参数是否有指定的属性和方法，
# 如果有就认定合适，而不关心对象的类型是否正确


# 课后作业
# 下面代码输出结果是什么？
# class People:
#     __name = "luffy"
#     __age = 18
# p1 = People()
# print(p1.__name, p1.__age)





# 报错，因为私有属性不能直接被访问



