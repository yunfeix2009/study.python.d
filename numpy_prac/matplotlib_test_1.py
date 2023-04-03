import numpy as np
from matplotlib import pyplot as plt
x = np.arange(-10, 11)
y = pow(x, 2)
x2 = np.arange(-10, 11)
y2 = -pow(x, 2)
x3 = np.arange(-10, 11)
y3 = -pow(x, 2)*np.sin(x)
plt.title('graph of quadratic function')
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y, '--b')
plt.plot(x2, y2, '-r')
plt.plot(x3, y3, '-g')
plt.show()