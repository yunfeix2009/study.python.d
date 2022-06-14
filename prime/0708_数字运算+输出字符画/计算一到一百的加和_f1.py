#计算一到一百偶数累加和。
#f1
num=0
for i in range(1,101):
    if i%2==0:
        num+=i
print('一到一百偶数累加和： %d'%num)