import numpy as np
from matplotlib import pyplot as plt
x = [5, 3, 7]
y = [1234, 326, 3]
x2 = [2, 8, -2]
y2 = [-123, -423, -4000]
plt.title('bar graph')
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.bar(x, y)
plt.bar(x2, y2)
plt.show()