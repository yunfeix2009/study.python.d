# 类的属性和方法及self

# 魔法方法__init__(作用和用法)



# 类的属性和方法及self
# 类里有属性和方法

# class Hero: # 定义一个英雄类,可以移动和攻击
#     def move(self):#实例方法
#         print("正在前往事发地点...")
#     def attack(self): #实例方法
#         print("发出了一招强力的普通攻击...")
#     def info(self):#self指代实例对象
#         print("英雄%s的生命值:%d"%(self.name,self.hp))
#         print("英雄%s的攻击力:%d"%(self.name,self.atk))
#         print("英雄%s的护甲值:%d"%(self.name,self.armor))
# daji = Hero()#实例化一个英雄对象,妲己
# 通过.给对象添加属性和对应的属性值
# daji.name = "妲己" # 姓名
# daji.hp = 2600 # 生命值
# daji.atk = 450 # 攻击力
# daji.armor = 200 # 护甲值
# daji.info()

# taidamier=Hero()# 实例化一个英雄对象,泰达米尔
# #给对象添加属性,以及对应的属性值
# taidamier.name="泰达米尔"
# taidamier.hp=3500 #生命值
# taidamier.atk=550 #攻击力
# taidamier.armor=100 #护甲值

# #通过.调用对象的实例方法
# taidamier.info()
# taidamier.move()
# taidamier.attack()

# 总结：一个类可以创建多个对象




# 刚刚是创建对象后添加属性
# 也可以在定义类时就拥有这些属性

# __init__()方法
# 魔法方法:两个下划线开始,两个下划线结束的方法
# __init__()就是一个魔法方法,还有__str__(),__del__()等等
# 意义：初始化实例
# 调用：创建对象后默认被调用,不需要手动调用
# 创建：1 如果类里没写__init__方法,python会自动创建
#       2 也可以自己定义__init__方法

# class Hero: #定义一个英雄类,可以移动和攻击
    # def __init__(self, name, skill, hp, atk, armor): 
    #     self.name = name# 英雄名       
    #     self.skill = skill# 技能      
    #     self.hp = hp # 生命值：       
    #     self.atk = atk# 攻击力
    #     self.armor = armor# 护甲值
    # def move(self):#实例方法
    #     print("正在前往事发地点...")
    # def attack(self): #实例方法
    #     print("发出了一招强力的普通攻击...")
    # def info(self):#实例方法
    #     print("英雄%s的生命值:%d"%(self.name,self.hp))
    #     print("英雄%s的攻击力:%d"%(self.name,self.atk))
    #     print("英雄%s的护甲值:%d"%(self.name,self.armor))
    #     print("英雄%s的技能:%s"%(self.name,self.skill))

# # 实例化对象时,__init__()默认被调用，参数会传递到对象的__init__()方法里
# taidamier = Hero("泰达米尔", "旋风斩", 2600, 450, 200)
# gailun = Hero("盖伦", "德玛西亚正义", 4200, 260, 400)
# taidamier.info()
# gailun.info()

# taidamier = Hero()
# taidamier.name="泰达米尔"
# taidamier.hp=3500 #生命值
# taidamier.atk=550 #攻击力
# taidamier.armor=100 #护甲值
# taidamier.skill="干饭" #技能
# taidamier.info()


# 课堂练习一：
# 定义一个学生类
# 学生有姓名(name)、年龄(age)、性别(sex),班级号(classNum)属性
# 提供displayInfo()方法显示这个学生的姓名、年龄、性别、班级号
# 创建两个学生对象,分别调用displayInfo()方法显示各自的信息。


class Student:
    def __init__(self,name,age,sex,classnum):
        self.name=name
        self.age=age
        self.sex=sex
        self.classnum=classnum
        print("init is called")
    def displayInfo(self):
        print('姓名：',self.name,'年龄：',self.age,'性别：',self.sex,'学号：',self.classnum)
#
# steven=Student('steven',11,'男',21)
# steven.displayInfo()
# linda=Student('linda',10,'女',21)
# linda.displayInfo()


# 课堂练习二：
# 定义一个学生类。
# 有下面的属性：
# 1 姓名
# 2 年龄
# 3 成绩(列表类型[语文，数学，英语],如[92,98,97],每课成绩的类型为整数)
# 实例方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 获取3门科目中的最高分：get_course() 返回类型:int
# 实例化一个学生对象，获取他的姓名，年龄和最高分数

class Student_plus:
    def __init__(self,name,age,scor):
        self.name=name
        self.age=age
        self.scor=scor
    def get_name(self):
        return ('姓名为：',self.name)

    def get_age(self):
        return ('年龄为：',self.age)
    def get_coures(self):
        return ('最高分为：',max(self.scor))
steven=Student_plus('steven',11,[95,98,100])
print(steven.get_name())
print(steven.get_age())
print(steven.get_coures())

0

