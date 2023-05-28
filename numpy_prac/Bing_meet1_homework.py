import math
import pandas as pd
import numpy as np

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def ways_back_to_origin(n):
    num = 0
    for i in range(0, n+1):
        if (i-(n-i)) % 5 == 0:
            num += nCr(n, i)
    return num
if __name__ == '__main__':
    for i in range(0, 100):
        ways = ways_back_to_origin(i)
        print(ways)