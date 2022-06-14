# 1魔法方法：__str__()和__del__()
# 2对象作属性
# 3继承




# 1魔法方法：__str__()和__del__()

# __str__()
# __str__(self)：# 参数：只有一个self
#   return str   # 要求：return一个字符串
# 用途：显示对象的描述信息
# print(对象)时
# 如果没有__str__方法,默认打印对象的内存地址
# 如果有__str__方法,打印__str__的返回值

class Hero:# 定义一个英雄类
    def __init__(self,name,skill):
        self.name=name#英雄名 实例变量
        self.skill=skill#技能 实例变量
    # def __str__(self):
    #     return "英雄<%s>的技能是%s"%(self.name,self.skill)
taidamier=Hero("泰达米尔","旋风斩")
gailun=Hero("盖伦","德玛西亚正义")
# print(taidamier)
# print(gailun)





# __del__()
# 创建对象时，python解释器默认调用__init__()方法
# 删除对象时，python解释器默认调用__del__()方法
#            python的内存回收会自动调用__del__()方法

class Hero:
    def __init__(self,name):#创建对象时会自动被调用
        print('__init__方法被调用')
        self.name=name
    def __del__(self):# 当对象被删除时，会自动被调用
        print("__del__方法被调用")
        print("%s被删除了"%self.name)
# taidamier=Hero("泰达米尔")
# del(taidamier)#删除对象,python内存回收会自动删除

# gailun = Hero("盖伦")
# gailun1 = gailun
# gailun2 = gailun
# print("%d被del()删除1次"%id(gailun))
# del(gailun)
# print("%d被del()删除1次"%id(gailun1))
# del(gailun1)
# print("%d被del()删除1次"%id(gailun2))
# del(gailun2)

# 引用计数：
# 每个对象都有一个引用计数器，记录有多少个变量引用这个对象
# 增加：当有变量保存了一个对象的引用时，引用计数加1
# 减少：当使用del()删除对象时，引用计数减1
# 当对象的引用计数为0时，对象才会被真正删除(内存被回收)



# 2对象作属性

# 案例:家里存放床
class Bed:#定义Bed类
    def __init__(self,area,name):
        self.name=name
        self.area=area
    def __str__(self):
        return self.name+'的面积为：'+str(self.area)
    def getUsedArea(self):#获取床的占用面积
        return self.area
    def getName(self):
        return self.name

class Home:#定义一个Home类
    def __init__(self,area):
        self.area=area#房间的可用面积
        self.containsItem=[]#房间容纳的物品，一个列表对象
    def __str__(self):#显示房间的可用面积和容纳的物品
        msg="当前房间可用面积为："+str(self.area)+" "
        if len(self.containsItem)>0:
            msg=msg+"容纳的物品有:"
            for temp in self.containsItem:
                msg=msg+temp.getName()+","
            msg=msg.strip(",")
        return msg
    def accommodateItem(self,item):  #容纳物品
        needArea=item.getUsedArea()#先获取物品的面积
        if self.area>=needArea:#如果家的可用面积大于等于物品的面积
            self.containsItem.append(item)
            self.area -= needArea
            print("ok：已经存放到房间中")
        else:
            print("err：房间可用面积为：%d,但存放当前物品需要的面积为%d"%(self.area,needArea))
newHome=Home(50)#创建一个家对象
print(newHome)
danrenchuang=Bed(20,'单人床')#创建一个床对象
print(danrenchuang)
newHome.accommodateItem(danrenchuang)#把床安放到家里
print(newHome)
shuangrenchuang=Bed(40,'双人床')#创建一个床对象
print(shuangrenchuang)
newHome.accommodateItem(shuangrenchuang)#把床安放到家里
print(newHome)


# 3
# 继承
# 现实中：一般指子女继承父辈的遗产
# 程序中：描述多个类之间的所属关系
# 类B继承类A: A是父类(基类,超类),B是子类(派生类)
# 表示：class 子类(父类)：
# 意义：子类继承了父类的属性和方法(父类的属性和方法可以在子类复用)


# class A:#父类
#     def __init__(self):
#         self.num=10
#     def print_num(self):
#         print(self.num+10)
# class B(A):#子类
#     pass
# b=B()
# print(b.num)
# b.print_num()




# 单继承：子类只继承一个父类

# 故事情节：
# 煎饼果子老师傅在煎饼果子界摸爬滚打几十年,
# 拥有一身精湛的煎饼果子技术，并总结了一套'古法煎饼果子配方'。
# 可是老师傅年迈已久,在临终之前希望把自己的配方传承下去，
# 于是老师傅把配方传给他的徒弟大猫



# class Master:#定义Master类
#     def __init__(self):    
#         self.kongfu="古法煎饼果子配方"#属性     
#     def makecake(self):#实例方法
#         print("按照<%s>制作了一份煎饼果子"%self.kongfu)


# class Prentice(Master):#['prentɪs]Prentice是子类，Master是父类
#     pass#子类继承父类所有的属性和方法
# laoli=Master()
# print(laoli.kongfu)
# laoli.makecake()
# damao=Prentice()#创建子类实例对象
# print(damao.kongfu)#子类对象可以直接使用父类的属性
# damao.makecake()#子类对象可以直接使用父类的方法

# 虽然子类没定义__init__方法,但父类有。
# 只要创建子类对象，就默认执行了从父类继承来的__init__方法



# 课后作业
# 下面的程序将得到什么结果？
# class Parent:
#     x = 1
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)


# 子类继承父类：
# 更改子类，不影响父类或其他子类
# 更改父类，直接继承没有修改的子类也跟着变