# # 字典 dict(dictionary)
#
# # 字典的定义:
# # 字典的访问:
#
#
#
# # 想一想
# # 有列表
# # nameList=['小明','小汪','光头强','熊大','熊二']
# # # "小汪"这个名字写错了,需要修改
# # nameList[1]='小王'
# # print(nameList)
#
#
# # 如果列表的顺序发生变化
# # nameList=['小明','光头强','小汪','熊大','熊二']
# # #此时需要修改下标,才能完成名字的修改
# # nameList[2]='小王'
# # print(nameList)
#
#
# # 如果列表的顺序发生变化,而且元素很多,并不知道"小汪"的位置
# # 那么就需要遍历列表,此时效率就相对低
#
#
# # 有没有既能存储多个数据,还能方便地定位到需要的元素的方法？
# # 答:字典
#
#
#
#
# # 字典的定义
# # 字典: 一系列的键值对(key=>value)
#
# # 格式: d = {key1:value1, key2:value2}
#     # 每个键值对用冒号:分割
#     # 各个对之间用逗号,分割
#     # 整个字典包括在花括号{}中
#
# # 特点:
# # 1 能存储多个元素
# # 2 每个元素由两部分组成,键:值
# # 3 可变
#
#
# # 举例:变量info为字典类型
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京'}
# # 'name':'班长'为一个元素,'name'为键,'班长'为值
#
#
# # 创建空字典
# # info= {}
# # info= dict()
#
#
# # info = ""
# # info = str()
#
# # info = []
# # info = list()
#
#
#
# # 字典的访问:根据键访问值
# # 1字典名[键名]     访问不存在的键会报错
# # 2字典名.get(键名) 访问不存在的键不报错(默认返回None),也可设定默认值
#
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京'}
# # print(info['name'])
# # print(info['address'])
# # print(info.get("name"))
#
# # 字典名[键名] 访问不存在的键会报错
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京'}
# # print(info['age'])
#
# # 字典名.get(键名) 访问不存在的键不报错
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京'}
# # print(info.get('age'))
#
# # 还可设定未找到的默认值
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京'}
# # print(info.get('age',18))
#
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京',"age":12}
# # print(info.get('age',18))
#
#
#
# # 课堂练习：
# # dict = {"k1":"v1","k2":"v2","k3":"v3","k4":"v4"}
# # 请获取字典中"k2"对应的值
# # 请获取字典中"k6"对应的值,如果不存在，不报错，让其返回None
#
# # print(dict['k2'])
# # print(dict.get('k6','v6'))
#
# # 字典 dict(dictionary)
#
# # 字典的定义:
# # 字典的访问:
#
#
#
# # 想一想
# # 有列表
# # nameList=['小明','小汪','光头强','熊大','熊二']
# # # "小汪"这个名字写错了,需要修改
# # nameList[1]='小王'
# # print(nameList)
#
#
# # 如果列表的顺序发生变化
# # nameList=['小明','光头强','小汪','熊大','熊二']
# # #此时需要修改下标,才能完成名字的修改
# # nameList[2]='小王'
# # print(nameList)
#
#
# # 如果列表的顺序发生变化,而且元素很多,并不知道"小汪"的位置
# # 那么就需要遍历列表,此时效率就相对低
#
#
# # 有没有既能存储多个数据,还能方便地定位到需要的元素的方法？
# # 答:字典
#
#
#
#
# # 字典的定义
# # 字典: 一系列的键值对(key=>value)
#
# # 格式: d = {key1:value1, key2:value2}
#     # 每个键值对用冒号:分割
#     # 各个对之间用逗号,分割
#     # 整个字典包括在花括号{}中
#
# # 特点:
# # 1 能存储多个元素
# # 2 每个元素由两部分组成,键:值
# # 3 可变
#
#
# # 举例:变量info为字典类型
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京'}
# # 'name':'班长'为一个元素,'name'为键,'班长'为值
#
#
# # 创建空字典
# # info= {}
# # info= dict()
#
#
# # info = ""
# # info = str()
#
# # info = []
# # info = list()
#
#
#
# # 字典的访问:根据键访问值
# # 1字典名[键名]     访问不存在的键会报错
# # 2字典名.get(键名) 访问不存在的键不报错(默认返回None),也可设定默认值
#
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京'}
# # print(info['name'])
# # print(info['address'])
# # print(info.get("name"))
#
# # 字典名[键名] 访问不存在的键会报错
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京'}
# # print(info['age'])
#
# # 字典名.get(键名) 访问不存在的键不报错
# info={'name':'班长','id':100,'sex':'f','address':'中国北京'}
# # print(info.get('age'))
#
# # 还可设定未找到的默认值
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京'}
# # print(info.get('age',18))
#
# # info={'name':'班长','id':100,'sex':'f','address':'中国北京',"age":12}
# # print(info.get('age',18))
#
#
#
# # 课堂练习：
# # dict = {"k1":"v1","k2":"v2","k3":"v3","k4":"v4"}
# # 请获取字典中"k2"对应的值
# # 请获取字典中"k6"对应的值,如果不存在，不报错，让其返回None
#
# # 字典的键值对
#
# # 字典的内置函数
# # len()
# # 获取：keys() values() items()
#
#
#
#
#
#
# # 字典的键值对
# # 1键唯一，值不需要唯一
# # 如果键重复，最后一个键值对会替换前面的
# # mydict={"a":1,"b":2,"b":1}
# # print(mydict['b'])#最后一个键值对会替换前面的
# # print(mydict)
#
# # 2键的数据类型只能是(字符串、数字、元组)，值的数据类型任意
#
# # dict1 = {'abc':123, 98.6:37, (1,2):'小明'}
# # print(dict1["abc"], dict1[(1,2)], dict1[98.6])
#
# # dict1 = {'abc':123, 98.6:37, [1,2]:'小明'}
# # print(dict1["abc"], dict1[(1,2)], dict1[98.6])
#
#
# # mydict = {["name"]:'小明', "age":7}
# # print(mydict[["name"]])
#
#
#
# # 字典的内置函数
#
# # len(dict) 返回字典的元素个数
# # dict1 = {'abc':123, 98.6:37, (1,2):'小明'}
# # print(len(dict1))
#
#
#
#
#
#
# # 获取
# # keys()以列表返回字典的所有键
# # dict1 = {'name':'小明','age':7,'class':'First'}
# # print(dict1.keys())
#
# # values()以列表返回字典的所有值
# # dict1 = {'name':7,'age':7,'class':'First'}
# # print(dict1.values())
#
# # items() 以列表返回字典的(键, 值)对
# # dict1 = {'name':'小明','age':7,'class':'First'}
# # print(dict1.items())
#
#
#del list[0]
#
# # 课堂练习
# mydict = {"k1":"v1","k2":"v2","k3":"v3","k4":"v4"}
# 请获取字典中所有的键
# 请获取字典中所有的值
# 请获取字典中所有的键值对

# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

#       字符串        列表             元组
# 增    '+'           append           '+'
# 删    del           del              del tupel
# 改    不支持        list[0]=0        不支持
# 查    print(str[0]) print(list[0])   print(tupel[0])
# 列表的修改: 用索引
# 列表的查找：in count() index()
# 列表的删除：del、pop()、remove()
# 添加元素：append() extend() insert()

# find()和index()
# 列表的删除：del、pop()、remove()
# del      (根据索引)删除元素   或 删除整个列表（删除后无法再访问）
# pop()    (根据索引)删除元素    并将删除的元素返回(没指定索引时，删除最后一个)
# remove() (根据元素的值)删除元素   (有多个相同的元素时,删除最左边的)
