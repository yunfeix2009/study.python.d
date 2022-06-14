# eval()的功能：将字符串str当成有效的表达式来求值并返回计算结果。如下是将字符串转换成方法名再调用：
def man():
    return "good job"


print(eval("man")())

# eval()可以把list, tuple, dict和string相互转化，这里以list为示例进行演示：
list1 = "[33,2,22,11,44,55]"
print(type(list1))
list2 = eval(list1)
print(type(list2))
print(list2)
print(list2[0])

tuple1 = "(33,2,22,11,44,55)"
print(type(tuple1))
tuple2 = eval(tuple1)
print(type(tuple2))
print(tuple2)
print(tuple2[0])

dict1 = "{1:33,2:2,3:22,4:11,5:44}"
print(type(dict1))
dict2 = eval(dict1)
print(type(dict2))
print(dict2)
print(dict2[1])



print( '结果为：',eval(input('请输入算式：\n')))