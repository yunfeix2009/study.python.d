# 查找：find()和index()
# 统计：count()
# 替换: replace()
# 分割：split()
# 判断字符类型：isalpha() isdigit() isalnum() isspace()


# 查找：查找某个子串在字符串里的索引
# find()和index()

# find():
# 用法：字符串.find(子串)
# 如果能找到，返回子串的索引（第一个字符的位置）
# 否则，返回-1
mystr='hello world python and pythoncpp'
print(mystr.find("world"))
mystr='hello world python and pythoncpp'
print(mystr.find("world1"))


# 可指定查找的开始位置和结束位置
# 用法：字符串.find(子串,开始位置,结束位置)
mystr='hello world python and pythoncpp'
print(mystr.find("python",0,5))
print(mystr.find("python",0,25))
print(mystr.find("python",0,len(mystr)))# 默认从左边开始找

mystr='hello world python and pythoncpp'
print(mystr.find("python",13,len(mystr)))

mystr='hello world python and pythoncpp'
print(mystr.find("python",0,10))


# rfind()
# 用法：类似于find()，不过是从右边开始查找
# mystr='hello world python and pythoncpp'
# print(mystr.rfind("python",0,len(mystr)))




# index()
# 用法：和find()类似
# 不同点:index()找不到子串时，抛出错误
mystr='hello world python and pythoncpp'
print(mystr.index("python"))
mystr='hello world python and pythoncpp'
print(mystr.index("python1"))



# 字符串.index(子串,开始位置,结束位置)
mystr='hello world python and pythoncpp'
print(mystr.index("python",0,len(mystr)))



# rindex()
# 用法：类似于index(),不过是从右边开始
mystr='hello world python and pythoncpp'
print(mystr.rindex("python",0,len(mystr)))



# 统计
# count()
# 统计子串在字符串里出现的次数
# 用法：字符串.count(子串)
mystr='hello world python and pythoncpp'
print(mystr.count("python"))
print(mystr.count("world"))
print(mystr.count("world1"))



# 可指定统计的开始位置和结束位置
mystr='hello world python and pythoncpp'
print(mystr.count("python",0,len(mystr)))
print(mystr.count("python",0,20))
print(mystr.count("python",0,10))




# 替换
# replace()
# 用法：字符串.replace(子串1,子串2)
# 用后边的替换前边的
name="hello world ha ha"
print(name.replace("ha","HA"))





# 可指定最大替换次数
# 用法：字符串.replace(子串1,子串2,最大替换次数)
name="hello world ha ha"
print(name.replace("ha","HA",1))



# 分割：
# split()  [splɪt]
# 以分割符分割字符串，返回列表
# 用法：字符串.spilt(分割符)
name="hello world ha ha"
print(name.split(" "))
name="hello world ha ha"
print(name.split("w"))




# 可指定最大分割次数
# 用法：字符串.spilt(分割符,最大分割次数)
name="hello world ha ha"
print(name.split(" ",1))
name="hello world ha ha"
print(name.split(" ",2))


# 判断字符类型：
# isalpha()     ['ælfə]
# 如果字符串的所有字符都是字母，则返回True,否则返回False
mystr="abc"
print(mystr.isalpha())
mystr="123"
print(mystr.isalpha())
mystr="abc 123"
print(mystr.isalpha())


# isdigit() ['dɪdʒɪt]
# 如果字符串的所有字符都是数字,则返回True，否则返回False
mystr="abc"
print(mystr.isdigit())
mystr="123"
print(mystr.isdigit())
mystr="abc123"
print(mystr.isdigit())



# isalnum()
# 如果字符串所有字符都是字母或数字,则返回True,否则返回False
mystr="abc"
print(mystr.isalnum())
mystr="123"
print(mystr.isalnum())
mystr="abc123"
print(mystr.isalnum())
mystr="abc 123"
print(mystr.isalnum())


# isspace()
# 如果字符串的所有字符都是空格，则返回True,否则返回False.
mystr=" "
print(mystr.isspace())
mystr="  "
print(mystr.isspace())
mystr="    "
print(mystr.isspace())
mystr="abc123"
print(mystr.isspace())


# 课堂练习
# 从键盘输入一行字符串
# 分别统计出其中英文字母，空格，数字和其他字符的个数



# python字符串常用操作2

# 大小写转换:capitalize() title() lower() upper()
# 判断开头结尾:startswith() endswith()
# 对齐:ljust() rjust() center()
# 删除空格：strip() lstrip() rstrip()
# 拼接字符串:join()



# 大小写转换
# capitalize()  ˈkæpɪtəlaɪz
# 把字符串的第一个字符转为大写
# mystr='hello world python and pythoncpp'
# print(mystr.capitalize())


# title()  [ˈtaɪtl]
# 把字符串的每个单词的首字母大写
# mystr='hello world python and pythoncpp'
# print(mystr.title())



# lower()  ['loɚ]
# 把字符串中所有大写字符转为小写
# mystr='Hello World python and pythoncpp'
# print(mystr.lower())

# upper()   
# 把字符串中所有小写字符转为大写
# mystr='Hello world python and pythoncpp'
# print(mystr.upper())




# 判断开头结尾
# startswith(str)
# 判断字符串是否以某个字符串开头，是则返回True,否则返回False
# mystr='hello world python and pythoncpp'
# print(mystr.startswith("h"))
# mystr='hello world python and pythoncpp'
# print(mystr.startswith("hello world"))
# mystr='hello world python and pythoncpp'
# print(mystr.startswith("ello"))




# endswith(str)
# 判断字符串是否以某个字符串结束，如果是返回True,否则返回False
# mystr='hello world python and pythoncpp'
# print(mystr.endswith('p'))
# mystr='hello world python and pythoncpp'
# print(mystr.endswith('cpp'))
# mystr='hello world python and pythoncpp'
# print(mystr.endswith('app'))





# 对齐
# rjust( )右对齐，长度不足，用空格填充
# mystr = "hello"
# print(mystr.rjust(10))

# ljust()左对齐，长度不足，用空格填充
# mystr = "hello"
# print(mystr.ljust(10))


# center() 居中，长度不足，用空格填充
# mystr = "hello"
# print(mystr.center(10))





# 删除字符串的空格
# strip()  删除字符串两端的空格[strɪp]
# mystr = '     hello    '
# print(mystr.strip())
# mystr = '     hello'
# print(mystr.strip())
# mystr = '     hel   lo  '
# print(mystr.strip())


# lstrip()删除字符串左边的空格
# mystr = '     hello'
# print(mystr.lstrip())
# mystr = '  hello   '
# print(mystr.lstrip())



# rstrip()删除字符串右边的空格
# mystr = '  hello   '
# print(mystr.rstrip())


# 课堂练习
# 写一个程序删除该字符串的所有空格，输出hello
# mystr = "   he   llo   "



# 思路：定义第二个字符串
# mystr1 =""
# for i in mystr:
#     if i != " ":
#         把i加到第二个字符串里





# 拼接字符串
# join()
# 用法："字符".join(字符串)
# 返回拼接后的新字符串
# print("-".join("python"))
#'p-y-t_2-h-o-n'





# 课堂练习
# 输入一个变量名
# 判断变量的命名是否符合规范
# 变量命名的规范：
# 1开头：不能是数字(只能是字母或下划线)
# 2内容：只能包含字母，数字和下划线

# 提示：循环 + else




