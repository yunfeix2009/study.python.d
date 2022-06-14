# 文件介绍

# 文件的打开与关闭


# 计算机文件:
# 举例：可以是文档、图片、程序等。
# 文件扩展名(后缀名):用于标识文件的类型(如图片常用的png、jpg，可执行文件exe等等)
# 作用：存储数据


# 文件的打开与关闭：
# 想一想：如果想用word写一份日记，应该有哪些流程呢？

# 1．打开word软件(新建一个word文件)
# 2．写入日记,保存文件
# 3· 关闭word软件



# 同样，python操作文件的过程与使用word写日记很相似
# 1．打开文件，或者新建一个文件
# 2．读/写数据(读：把文件里的内容读到程序里，写:把程序里的内容写到文件里)
# 3．关闭文件


# f = open(文件名,访问模式,编码) # 打开一个已经存在的文件，或者创建一个新文件
# f.read() # 读取文件
# f.close()  # 关闭这个文件

# 访问模式    说明         文件已存在            文件不存在
# r      只读（默认）    从文件的开头开始读        返回异常
# w      创建写          将其覆盖                创建新文件
# a      追加写         从文件的结尾接着写        创建新文件
# x      排他写          返回异常                创建新文件

# r模式
# 读取test.txt文件
# f=open("test1.txt",'r',encoding="utf-8")#encoding="utf-8"是指定中文的编码
# content=f.read()#读取文件内容
# print(content)
# f.close()



# w模式
# f=open("test2.txt",'w',encoding="utf-8")
# f.write("少壮不努力，老大徒伤悲11111111") # 写入文件,如果原文件有内容，会覆盖原来的内容
# f.close()




# a模式
# f=open("test.txt",'a',encoding="utf-8")
# f.write("好好学，人工智能首选语言\n")#写入文件,会接着写
# f.close()


# x模式
# f=open("test1.txt",'x',encoding="utf-8")
# f.write("好好学，人工智能首选语言\n")#写入文件,如果源文件已存在会报错
# f.close()



# 课堂练习:
# 写一篇日记,保存到文件中,并读出来输出到终端
# 文件名格式为" 姓名(xxx)-日期(年-月-日)的一天",以txt为后
# import os
# if not os.path.exists("日志") :
#     os.mkdir("日志")
# myfile=open('日志/steven-2020年11月21日.txt','w',encoding='UTF-8')
# myfile.write(
# '''
# 2020年11月21日 日记
#                 大雪
# 我今天吃了早饭
# 我今天吃了午饭
# 我今天吃了晚饭
# '''
# )
# myfile.close()
# myfile=open('日志/steven-2020年11月21日.txt','r',encoding='UTF-8')
# content=myfile.read()
# print(os.path.abspath(''))
# print('日志文件保存在这个目录下的[%s]这个地址[%s]'% (os.path.abspath('') , myfile.name))
# print(content)
# myfile.close()


# 写一个记日记的小程序，
# 功能：
# 1.输出今天的日期
# 2.可以从终端输入文字，回车后可以继续输入
# 直到输入end时停止，并将之前输入的内容存入以当前日期命名的文件
# 提示：
# 1可以使用追加写
# 2换行符是"\n"
# import time
#
# print(time.strftime("today is %Y-%m-%d"))
# myfile=open('日记teven-2020年11月21日.txt','a',encoding='UTF-8')
# while True:
#     content=input('输入你的日记，如果你想停止就输入end:')
#     myfile.write(content + '\n')
#     if content=='end':
#         break


## 1
### 去除列表中的重复元素
# L = ['b','c','d','c','b','a','a']
# list=[]
# for i in L:
#     if i in list:
#         pass
#     else:
#         list.append(i)
# print(list)
### 提示：新建一个空列表，没在空列表里则添加到空列表中


### 2
### 有如下值需要保存到字典里
# li=[11,22,33,44,55,66,77,88,99,90]
### 将所有大于66的值保存至字典的第一个key中
### 将小于66的值保存至第二个key的值中
### 即:{'k1':大于66的所有值列表,'k2':小于66的所有值列表}
# dict={'k1':[],'k2':[]}
# for i in li:
#     if i > 66:
#         dict['k1'].append(i)
#     elif i < 66:
#         dict.get('k2').append(i)
# print(dict)






