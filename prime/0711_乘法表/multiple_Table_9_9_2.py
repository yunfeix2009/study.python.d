i=1
while i<10:
    # for j in range(1,i+1):
    j=1
    while j<i+1:
        print('%d*%d=%-2d '%(j,i,i*j),end='',sep=' ')
        j+=1
    print()
    i+=1