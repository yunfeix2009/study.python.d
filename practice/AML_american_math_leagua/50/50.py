import random
for i in range(1,11):
    list=[]
    list_all=[]
    for j in range(2**(i-1)):
        list.append(random.randint(1,2))
    for item in list:
        flag=0
        if item==1:
            if flag==0.5:
                break
            else:
                flag=0.5
        else:
            flag=0
    else:
        list_all.extend(list)

    print(i,len(list_all)/i,list_all)