# 200中所有的质数
def isPrimaryNumber(n):
    if n<2 :
       return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True
N = 200 # you can change to input a number
print("Prime number in %d !" %N)


# 找都质数列中公差为Delta的等差数列
list = []   
for i in range(1,N + 1):
    if isPrimaryNumber(i):
        print("%2d " %i, end='')
        list.append(i)
print()
for x in list:
    for d in range(1,20):
        for i in range(0,5):
            if x + i*d not in list:
                break
        else:
            print('Queue', end=':')
            for i in range(0,5):
                print(x + i*d,end='->') 
            print()
            print('Delta:',d)         