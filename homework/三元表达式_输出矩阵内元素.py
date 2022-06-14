a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b= [j for i in a for j in i]
list=[]
for i in b:
    if i%2==0:
        list.append(i)
print(list)
print([i for i in range(10)])

# c="条件成立" if a>b else "条件不成立"
