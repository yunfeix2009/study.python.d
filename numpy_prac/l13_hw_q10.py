number=0
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):
                for e in range(1, 7):
                    if len(list(set([a, b, c, d, e])))>=3 and not '16' in str(e+10*d+100*c+1000*b+10000*a) and not '61' in str(e+10*d+100*c+1000*b+10000*a):
                        print(str(e+10*d+100*c+1000*b+10000*a))
                        number+=1

print("number: %s", number)