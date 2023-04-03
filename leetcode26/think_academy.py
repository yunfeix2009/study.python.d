sum = 0
for i in range(100000, 999999):
    if i//1000 == i%1000 and i%1000//100+i%100//10+i%10 == 10:
        sum+=i
        print(i)
print(sum)
print(sum/13)
print(111111/13)
print(11111/13)
120120
120102
120