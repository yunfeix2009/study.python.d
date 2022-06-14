fruit=['苹果','桃子','梨','香蕉','橙子','猕猴桃','榴莲','橙子','苹果']
# for i in fruit:
#     if i=='橙子':
#         pass
#     else:
#         print(i)
i=0
fruit.append('苹果')
fruit.insert((len(fruit))//2,'苹果')
fruit.insert(11,'苹果')
while i<len(fruit):
    if fruit[i]=='橙子':
        fruit[i]='柠檬'
        print(fruit[i])
    else:
        print(fruit[i])
    i+=1