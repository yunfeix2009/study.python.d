# 100内不是7的倍数的数的和
num=0
for i in range(1,101):
    if i%7==0:
        continue
    num+=i
print(num)