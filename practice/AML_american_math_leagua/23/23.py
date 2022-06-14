fanlyList=[]
for n in range(1,11):
    for i in range(n*1000000000,(n+1)*1000000000):
        i_str = str(i)
        if i%1000000==0:
            print('----------:'+i_str)
        for j in range(10):
            j_str=str(j)
            if i_str.count(j_str)!=int(i_str[j]):
                break
        else:
            print('---------------------------------------------------------',i)
            fanlyList.append(i)
for i in range(3):
    print(' ')
print(fanlyList)
