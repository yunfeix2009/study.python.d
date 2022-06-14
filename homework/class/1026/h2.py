import random
list_2=[]
list_1=list(range(2,102,2))
for i in range(1,11):
    a=random.choice(list_1)
    list_2.append(a)
list_2.sort(reverse=True)
list_print=list_2[0:5]
print(list_print)