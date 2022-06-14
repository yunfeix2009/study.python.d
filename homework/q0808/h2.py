list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
temp=0
def change():
    list[0:22], list[22], list[23],list[24]=list[3:25],list[2],list[1],list[0]
while True:
    temp+=1
    change()
    print(list)
    if list==[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]:
        print(temp)
        break