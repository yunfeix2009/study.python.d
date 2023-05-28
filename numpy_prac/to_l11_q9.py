import math

def is_perfect_square(num):
    sqrt = math.sqrt(num)
    return sqrt.is_integer()
print(is_perfect_square(49))
for i in range(1, 1000):
    if is_perfect_square(pow(i, 2)+5*i+13):
        print(i)