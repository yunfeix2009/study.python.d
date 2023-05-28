import numpy as np
from matplotlib import pyplot as plt
def fibonacci(n):
    if n <= 0:
        return []

    sequence = [0]
    if n == 1:
        return sequence

    sequence.append(1)
    if n == 2:
        return sequence

    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)

    return sequence


array_fibonacci = fibonacci(100)
x = np.arange(0, 100)
print('x:', x)
y_exponential = [pow(1.618, x) for x in range(0, 100)]
print('y_exponential:', y_exponential)
y_fibonacci = array_fibonacci
print('y_fibonacci:', y_fibonacci)

plt.title('bar graph')
plt.xlabel("x axis caption")
plt.plot(x, y_fibonacci, "-r")
plt.plot(x, y_exponential, "-g")
plt.show()