import numpy as np
from matplotlib import pyplot as plt
x = np.random.randint(-100, 100, 5)
print('x:', x)
y = np.random.randint(-100, 100, 5)
print('y:', y)

plt.title('bar graph')
plt.xlabel("x axis caption")
plt.bar(x, y)
plt.show()