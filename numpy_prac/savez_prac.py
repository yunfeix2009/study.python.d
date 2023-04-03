import numpy as np

# a = np.arange(6).reshape(2, 3)
# b = np.arange(0, 1.0, 0.1)
# c = np.sin(b)
# np.savez('sin_values', a=a, b=b, sin_array=c)
# r = np.load('sin_values.npz')
# print('r.files:', r.files)
# print('a:', r['a'])
# print('b:', r['b'])
# print('c:', r['sin_array'])



# d = np.ones(16).reshape(4, 4)
# e = np.zeros(16).reshape(4, 4)
# f = np.empty(16).reshape(4, 4)
#
# np.savez('matrix_1', ones=d, zeros=e, empty=f)
# matrixes = np.load('matrix_1.npz')
#
# print('np.files:', matrixes.files)
# print('ones_matrix:')
# print(matrixes['ones'], '\n')
# print('zeros_matrix:')
# print(matrixes['zeros'], '\n')
# print('empty_matrix:')
# print(matrixes['empty'])



# g = np.array([1, 5, 3, 7, 2, 7, 2])
# h = np.array([78, 3, 876, 23, 87, 32, 65])
# np.savez('sample_data', g, h)
# sample_data = np.load('sample_data.npz')
# print(sample_data['arr_0'])
# print(sample_data['arr_1'])

i = np.arange(100).reshape(4, 25)
np.savetxt('numbers_txt_format', i)
i_load = np.loadtxt('numbers_txt_format')
print(i_load)