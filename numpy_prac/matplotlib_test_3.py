import numpy as np
from matplotlib import pyplot as plt
x = np.arange(-10000, 10000)
y = pow(x, 3)
plt.title('graph of quadratic function')
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y, '--g')
plt.show()