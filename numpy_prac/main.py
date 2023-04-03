import numpy as np
a = np.arange(10).reshape(2, 5)
np.save('outfile.npy', a)
np.save('outfile2', a)
a_in_file = np.load('outfile.npy')
a_in_file2 = np.load('outfile2.npy')
print(a_in_file)
print(a_in_file2)