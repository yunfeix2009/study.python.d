# 字典常见操作(增刪改查)


# 查找：     get()     字典名[键]
# 增加/修改：update()  字典名[键]
# 删除：     del popitem() clear()



# 查找
# 1 通过键查找值
# dict1 = {'name':'小明','age':7,'class':'First'}
# print(dict1["name"])

# 2 get()查找指定键对应的值
# dict.get(key)
# dict1 = {'name':'小明','age':7,'class':'First'}
# print(dict1.get("name"))


# 如果键不存在，返回默认值None
# dict1 = {'name':'小明','age':7,'class':'First'}
# print(dict1.get("school"))

# 可以指定找不到时返回的值
# dict1 = {'name':'小明','age':7,'class':'First'}
# print(dict1.get("school","实验小学"))


# 修改和添加：
# 1 字典名[键]=值
# 2 字典.update(新字典)
# 存在的key则修改，不存在的key则添加

# info={'name':'班长','id':100,'sex':'f','address':"中国北京"}
# info['id']= 99
# print("修改后",info)

# info={'name':'班长','id':100,'sex':'f','address':"中国北京"}
# info['school']="实验小学"# 如果这个key不存在，会新增这个元素
# print(info)

# mydict = {'Name':'小王','Age':7}
# dict1 = {'Name':'小白'}
# mydict.update(dict1)
# print(mydict)

# mydict = {'Name':'小王','Age':7}
# dict1 = {'Sex':'female'}
# mydict.update(dict1)
# print(mydict)




# 删除元素：三种方法
# del  根据键删除某个元素  或 删除整个字典（删除后无法再访问）
# popitem():删除并返回最后一个键值对
# clear():删除字典的所有元素(清空)

# del
# info={'name':'班长','id':100,'sex':'f','address':"中国北京"}
# del info["address"]#删除某个元素
# print(info)

# info={'name':'班长','id':100,'sex':'f','address':"中国北京"}
# del info #删除整个字典
# print(info)

# popitem()
# info={'name':'班长','id':100,'sex':'f','address':"中国北京"}
# print(info.popitem())#删除并返回最后一个键值对
# print(info)


# 如果字典为空,报错
# dict1 = {}
# print(dict1.popitem())

# clear()
# info={'name':'班长','id':100,'sex':'f','address':"中国北京"}
# info.clear()#删除字典的所有元素(清空)
# print(info)


# 字典的应用：
# 用字典统计列表里各个元素出现的次数
# mylist = ["a","c","b","c","d","b","c"]
# mydict = {}# 字典的键就是要统计的元素，值就是该元素出现的次数
# for i in mylist:
#     mydict[i]=mydict.get(i,0) +1
# print(mydict)


# 课堂练习：
# 现有dict2 = {"k1":"v11","a":"b"}
# 通过操作使dict2 = {"k1":"v1","a":"b","k2":"v2"}
# dict3={'k2':'v2'}
# dict2 = {"k1":"v11","a":"b"}
# dict2['k1']='v1'
# dict2.update(dict3)
# print(dict2)

# 课后作业：
# 从字符串'abcdefg'中随机选两个字母组成新字符串(可重复),
# 共选100组，这100组里会有很多重复的字符串
# 要求：用字典统计字符串出现的次数，输出所有不同的字符串及其重复的次数

# import random
# str_1='abcdefg'
# list=[]
# dict={}
# for i in range(1,101):
#     str=random.choice(str_1) + random.choice(str_1)
#     dict[str] = dict.get(str, 0) + 1
# for i in list:
# print(dict)
# print(sum(dict.values()))

# 思路：字符串当作键，出现的次数当作值，需要用到字典的get方法
# 随机选择：random.choice()
# choice()随机选择序列里的一个元素
import random
# print(random.choice([1,2,3,4,5]))
# print(random.choice("hello"))

# 课堂练习
# 两种方式实现带索引的遍历：
chars = ['a', 'b', 'c', 'd']
# 输出示例：
# 0 a
# 1 b
# 2 c
# 3 d

for i,j in enumerate(chars):
    print(i,j)
j=0
for i in chars:
    print(j,i)
    j+=1