# 判断是否是质数
def primary(x):
    if x==1:
        return False
    else:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return False
        else:
            return True

# 计算100以内的质数加和
num=0
for i in range(1,101):
    if primary(i):
        num+=i
print(num)
