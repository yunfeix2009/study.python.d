# 继承

# 单继承
# 多继承
#   多继承重名问题
#   子类中调用重写的同名父类方法
# 多层继承


# 剧情发展：(多继承)
# 大猫掌握了师傅的配方，可以制作古法煎饼果子
# 但是大猫是个爱学习的好孩子，他希望学到更多的煎饼果子的做法
# 于是通过网上搜索，找到了一家煎饼果子培训学校


# 多继承
# 定义：子类继承了多个父类(继承了所有父类的属性和方法)
# 重名问题：多个类之间方法名或属性名相同时用哪个？
#     分类：
#         1多个父类之间重名：
#         2子类和父类之间重名：也叫重写(子类重写父类的同名属性或方法)
#     解决方式：根据子类的__mro__属性的顺序查找(Method Resolution Order)
#         先子类，再按继承的父类顺序从左到右

# 多个父类之间方法名或属性名相同：
class Master:#定义Master类
    def __init__(self):    
        self.kongfu="古法煎饼果子配方" 
    def makecake(self):#实例方法
        print("按照<%s>制作了一份煎饼果子"%self.kongfu)
    def dayandai(self):
        print("师傅的大烟袋")
class School:#定义School类
    def __init__(self):
        self.kongfu="现代煎饼果子配方"
    def makecake(self):
        print("按照<%s>制作了一份煎饼果子"%self.kongfu)
    def xiaoyandai(self):
        print("学校的小烟袋")
class Prentice(School,Master):#多继承，继承多个父类(School在前)
    pass



# damao=Prentice()
# print(Prentice.__mro__)#根据子类的魔法属性__mro__的顺序查找
# print(damao.kongfu)#执行School的属性
# damao.makecake()#执行School的实例方法
# damao.dayandai()
# damao.xiaoyandai()


class Prentice(Master,School):#多继承，继承多个父类(Master在前)
    pass

# damao=Prentice()
# print(Prentice.__mro__)#根据子类的魔法属性__mro__的顺序查找
# print(damao.kongfu)#执行Master的属性
# damao.makecake()#执行Master的实例方法



# 重写：子类重写父类的同名属性或方法
# 剧情发展：
# 大猫掌握了师傅的配方和学校的配方，通过研究，大猫在两个配方的基础上，
# 创建了一种全新的煎饼果子配方，称之为"猫氏煎饼果子配方"。

class Master:#定义Master类
    def __init__(self):    
        self.kongfu="古法煎饼果子配方"    
    def makecake(self):
        print("按照<%s>制作了一份煎饼果子"%self.kongfu)
class School:#定义School类
    def __init__(self):
        self.kongfu="现代煎饼果子配方"
    def makecake(self):
        print("按照<%s>制作了一份煎饼果子"%self.kongfu)
class Prentice(School,Master):
    def __init__(self):    
        self.kongfu="猫氏煎饼果子配方"    
    def makecake(self):#实例方法
        print("按照<%s>制作了一份煎饼果子"%self.kongfu)
# damao=Prentice()
# print(Prentice.__mro__)#根据子类的魔法属性__mro__的顺序查找
# print(damao.kongfu)#子类和父类有同名属性，默认使用子类的
# damao.makecake()#子类和父类有同名方法，默认使用子类的


# 子类重写父类
class A:
    def dayin(self):
        print('A')
class B:
    def dayin(self):
        print('B')
class C(A,B):
    def dayin(self):
        print('C')
# c = C()
# c.dayin()
# print(C.__mro__)



# 重写后的子类方法中如何调用父类方法？
# 方法一：父类名.父类方法()
# 方法二：super().父类方法()

# 方法一：父类名.父类方法
class A:
    def dayin(self):
        print('A')
class B:
    def dayin(self):
        print('B')
class C(A,B):
    def dayin(self):
        A.dayin(self)
        B.dayin(self)
        print('C')
# c = C()
# c.dayin()




# 方法二：super().父类方法()
# super()用于调用父类(超类)
# 1指定类名时，调用指定类后面的类的方法
# 2不写参数时，调用当前类后面的类的方法

# super实例
class A:
    def dayin(self):
        print('A')
class B:
    def dayin(self):
        print('B')
class C(A,B):
    def dayin(self):
        # 1指定类名时，调用指定类后面的类的方法
        # super(C,self).dayin()#调用C类后面的类的dayin()
        # super(A,self).dayin()#调用A类后面的类的dayin()
        # 2不写参数时，调用当前类后面的类的方法
        super().dayin()#调用当前类后面的类的dayin()
        print('C')
# c = C()
# c.dayin()
# print(C.__mro__)


# 总结：继承不止两个类时，如果要调用某个类的方法，只需知道上一个类名就行



# 课堂练习：
# 编写程序，A继承B,两个类都实现了handle方法，handle方法里输出类名
# 在A的handle方法中调用B的handle方法

class B:
    def handle(self):
        print('B')
class A(B):
    def handle(self):
        B.handle(self)
a=A()
b=B()
a.handle()
b.handle()






# 多层继承
# 定义：子类继承的父类还继承了其它父类
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B):
#     pass
# class E(B):
#     pass
# class F(D,E):
#     pass
# print(F.__mro__)#FDEBA

# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B):
#     pass
# class E:
#     pass
# class F(D,E):
#     pass
# print(F.__mro__)#FDBAE




# 每个类的__init__方法会调用该类后面的类的__init__方法
class A:
    def __init__(self):
        print('A')
        super(A,self).__init__()
class B:
    def __init__(self):
        print('B')
        super(B,self).__init__()
class C(A):
    def __init__(self):
        print('C')
        super(C,self).__init__()
class D(A):
    def __init__(self):
        print('D')
        super(D,self).__init__()
class E(B,C):
    def __init__(self):
        print('E')
        super(E,self).__init__()
class F(C,B,D):
    def __init__(self):
        print('F')
        super(F,self).__init__()
class G(D,B):
    def __init__(self):
        print('G')
        super(G,self).__init__()
# g=G()#创建对象时会运行初始化方法__init__()
# print(G.mro())# GDAB
# f=F()
# print(F.mro())# FCBDA




# 课堂练习
# 下面代码执行结果是什么？
class A:
    def __init__(self):
        print("EnterA")
        print("LeaveA")
class B(A):
    def __init__(self):
        print("EnterB")
        super(B,self).__init__()
        print("LeaveB")
class C(A):
    def __init__(self):
        print("EnterC")
        super(C,self).__init__()
        print("LeaveC")
class D(A):
    def __init__(self):
        print("EnterD")
        super(D,self).__init__()
        print("LeaveD")
class E(B,C,D):
    def __init__(self):
        print("EnterE")
        super(E,self).__init__()
        print("LeaveE")
# print(E.mro())
# E()
