for a in range(1, 6):
    for b in range(1, 6):
        if b!=a:
            for c in range(1, 6):
                if c!=a and c!=b:
                    for d in range(1, 6):
                        if d!=a and d!=b and d!=c:
                            for e in range(1, 6):
                                if e!=a and e!=b and e!=c and e!=d:
                                    if b<=(a+c)/2 and c<=(b+d)/2 and d<=(c+e)/2:
                                        print(a, b, c, d, e)