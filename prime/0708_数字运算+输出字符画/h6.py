j=1
while j<=10:
    i = 1
    while i<=10:
        if j%2==1:
            print('★',end='')

        else:
            print('♥ ',end='')
        i += 1
    print('\n',end='')
    j+=1