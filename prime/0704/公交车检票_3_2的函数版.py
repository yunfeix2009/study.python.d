def byBus(monny, people, howMeny, howMenyPeople):
    if people<=0 or howMenyPeople<=0 or howMeny<=0 or howMeny-howMenyPeople<people or howMeny<howMenyPeople:
        print('参数不对。')
    elif  monny<=2*people or howMeny-howMenyPeople<people:
        print('不能上公交车')
    else:
        print('能上公交车')
byBus(10,3,30,15)