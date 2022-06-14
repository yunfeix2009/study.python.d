# 1面向对象与面向过程

# 2类和对象(类的定义及实例化)










# 1面向对象与面向过程

# 面向对象和面向过程：都是一种编程思想，一种解决问题的方式

# 面向对象：核心是对象，强调万物皆对象
# 面向过程：核心是过程，强调过程和步骤

# 举例1：把大象放冰箱

# 面向过程的方式：分三步
# 1把冰箱门打开
# 2把大象装进去
# 3把冰箱门关上
# 像这种一步一步去做的思路就是面向过程

# 面向对象的方式：找一个比较牛的冰箱
# 可以自己开门，自己把大象装进去，自己关门
# 像这样找一个对象来帮我们解决问题的思路就是面向对象



# 举例2：需要买个电脑
# 面向过程的方式:
# 第一步，看自己有多少钱
# 第二步，需要选一个什么样的电脑
# 第三步，去哪买
# 第四步，怎么去
# 第五步，到了卖电脑的地方要砍价，砍半天，最后砍了一块钱
# 第六步，想想就这样吧，最后买了
# 第七步，给钱，拿电脑回家吃饭


# 面向对象的方式
# 找一个人（电脑高手）帮我们做这件事
# 只需要给钱并告诉他买个什么样电脑即可，其他的不用关心


# 面向对象思想的特征
# 1）更符合我们的思想行为习惯
# 2）将我们从执行者变成了指挥者(指挥对象做事情)
# 3）更简单



# 2 类与对象

# 都是面向对象程序设计中最基础的组成单元
# 类：具有相同特征和行为的一类事物
# 对象：是这类事物中具体的一个

# 比如：有一个动物园
# 动物园里的每一种动物就是一个类：老虎、天鹅、鳄鱼、熊。
# 他们有相同的特征：比如身高、体重、出生时间和品种，
# 还有各种行为：比如鳄鱼会游泳，天鹅会飞，老虎会跑能会吃

# 类：这些老虎、熊等都不是具体的某一只，而是一类动物。
# 对象：具体的一只老虎就是一个具体的实例，一个对象。


# 区别：
# 类：是对象的模板(是抽象的)
# 对象：是类的实例(是具体的)(实例就是对象)
# 一个类可以有多个对象


# 请区别以下类和对象：
# 人
# 某学校某班的小明 
# 苹果
# 放在桌子上的那个苹果
# 汽车
# 奔驰汽车
# 书籍
# python书籍
# 小明手里拿的那本书



# 类(class)的定义和实例化

# 类的定义：
# 类里包含属性和方法(属性又叫特征，方法又叫行为)
# 格式：
# class 类名: #类名首字母习惯上要大写
#     def __init__(self, 属性, …): # 用于初始化实例
#         pass # self指代实例(对象)
#     def 方法名1(self, 参数, …): # 方法1
#         pass
#     def 方法名2(self, 参数, …): # 方法2
#         pass

# 例如：定义一个人类
# class Person:# 类名Person
#     def __init__(self, age, weight):
#         # age,weight是类的属性
#         self.age = age
#         self.weight = weight
#     def eat(self): # eat()是类的行为
#         print("我吃了")

# 类的实例化
# 就是把类实例化为对象
# 格式：类名(属性1，属性2)
# p = Person(16, 60)
# p.eat()
# print("p的年龄",p.age)

# p1 = Person(10, 40)
# print("p1的年龄",p1.age)

# p2 = Person(13, 45)
# p2.eat()
# 一个类可以创建多个对象
# 类的特征和行为在实例化出的对象中依旧存在
# p p1 p2都是Person类的实例（对象），都有age和weight属性以及eat()行为


# 课堂练习
# "Joker 在 BMW 4S 店买了一俩 BMW X7"，根据业务描述，定义相关类。

# 提示：
# 类名         属性                方法
# 人类：       人的名字             买车
# 汽车商店类：  商店名字
# 汽车类：      汽车名字，商店名字

# class Person:# 类名Person
#     def __init__(self, age, weight):
#         # age,weight是类的属性
#         self.age = age
#         self.weight = weight
#     def eat(self): # eat()是类的行为
#         print("我吃了")
# p = Person(16, 60)
# p.eat()
# print("p的年龄",p.age)

# p1 = Person(10, 40)
# print("p1的年龄",p1.age)

# p2 = Person(13, 45)
# p2.eat()

class Person:
    def __init__(self,person_name):
        self.person_name=person_name
    def buy_car(self):
        print(self.person_name,'买了车')
class Shop:
    def __init__(self,shop_name):
        self.shop_name=shop_name
class Car:
    def __init__(self,car_name,shop_name):
        self.car_name=car_name
        self.shop_name=shop_name

p=Person('steven')
p.buy_car()

