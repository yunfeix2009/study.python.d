# 魔法方法__new__


# 单例模式




# __new__()
# 负责创建类实例的静态方法(无需用staticmethod装饰器修饰)
# 执行时机：优先__init__()初始化方法被调用

#        __new__()                  __init__()
# 作用:  创建类实例                  初始化实例
# 时间: 实例创建前被调用       实例创建后被调用(__init__在__new__之后运行)
# 第一个参数:cls(就是要实例化的类)    self(就是__new__返回的实例)
# 返回值:必须有,返回实例化出来的对象   不需要
#     通常return父类__new__出来的实例

class A(object):
    def __init__(self):
        print("init方法被运行")
    def __new__(cls):
        print("new方法被运行")
        return object.__new__(cls)
# A()



# 课堂练习：
# 下面代码输出结果是什么？
class MagicDemo:
    def __init__(self):
        print("call __init__ second")
        self.value=[1,2,3]
    def __new__(cls):
        print("call __new__ first")
        return super(MagicDemo,cls).__new__(cls)
    def __del__(self):
        print("call __del__")
    def __str__(self):
        return "call __str__"
# mag=MagicDemo()
# print(mag.value)
# print(mag)
# del mag




# 单例模式
# 单例模式是设计模式的一种
# 单例类：确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例


# 举例：电脑回收站
# 在整个操作系统中，回收站只能有一个实例，整个系统都使用这个唯一的实例，
# 而且回收站自行提供自己的实例。



# 实例化一个单例
class Singleton(object): 
    __instance = None #类的实例
    def __new__(cls, *args):
        #如果类属性__instance的值为None,就创建一个对象，并赋值给__instance
        #如果不为None,就直接返回这个对象
        #这样就保证了内存中只有1个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self, age,name):
        self.age = age
        self.name = name
# b=Singleton(8,"xiaoming")
# a=Singleton(18,"xiaoming")# __new__  __init__
# print(a.age)
# print(b.age)

# print(id(a))
# print(id(b))

# a.age=19 #给a指向的对象修改属性
# print(a.age)#获取a指向的对象的age属性
# print(b.age)#获取b指向的对象的age属性


class Singleton(object): 
    __instance = None 
    __is_first = True #是否第一次调用__init__
    def __new__(cls, *args):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self, age,name):# 创建单例时，__init__方法只执行1次
        if Singleton.__is_first:
            self.age = age
            self.name = name
            Singleton.__is_first = False
a=Singleton(18,"xiaoming")
b=Singleton(8,"xiaoming")
# print(a.age)
# print(b.age)

# print(id(a))
# print(id(b))
# a.age=19 #给a指向的对象添加一个属性
# print(a.age)#获取a指向的对象的age属性
# print(b.age)#获取b指向的对象的age属性




# 课堂练习：
# 设计一个小游戏
# 有2个角色:人和妖怪，2个角色的名字，生命值，攻击力不一样
# 游戏开始：出现2个人、3只妖怪，
# 他们互相仇视敌方,人被妖怪伤害会掉血，妖怪被人伤害也会掉血

class Animal:#动物类
    def __init__(self,name,lifevalue,aggressivity):
        self.name=name#名字
        self.lifevalue=lifevalue#生命值
        self.aggressivity=aggressivity#攻击力
    def attack(self,enemy):#攻击
        enemy.lifevalue -= self.aggressivity
        print(self.name,'attcak',enemy.name)
class People(Animal):#人类
    camp='home'#家
    def attack(self,enemy):
        super().attack(enemy)
class Dog(Animal):#妖怪类
    camp="wo"#营地
    def attack(self,enemy):
        super().attack(enemy)
p1=People('alice',80,30)
p1=People('alex',80,30)
d1=Dog('d1',90,50)
d2=Dog('d2',90,50)
d3=Dog('d3',90,50)

# print(p1.name,"的生命值",p1.lifevalue)
# d1.attack(p1)
# print(p1.name,"的生命值",p1.lifevalue)

# print(d1.name,"的生命值",d1.lifevalue)
# p1.attack(d1)
# print(d1.name,"的生命值",d1.lifevalue)
