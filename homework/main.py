import sys
with open("./a.txt","w",encoding="utf-8") as f:
    sys.stdout = f
    for i in range(1,10):
        for j in range(1,i+1):
            print("{}x{}={} ".format(j,i,i*j),end="")
        print()
