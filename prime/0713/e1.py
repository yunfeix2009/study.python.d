# 交换变量


#f1
a,b=3,5
b,a=a,b
print(a,b)

#f2
a,b=3,5
a=a+b
b=a-b
a=a-b
print(a,b)

#f3
a,b=3,5
temp=a
a=b
b=temp
print(a,b)