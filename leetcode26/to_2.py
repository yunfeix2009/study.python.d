# from numpy import cbrt

# for i in range(1, 100000):
#     # if ((3*pow(i, 2)+3*i+7)** (1./3))%1 == 0:
#     if int(pow(i, 2) ** (1./3)) == pow(i, 2) ** (1./3):
#         print(i)

# limit = 1000  # set the upper limit for n
#
# for n in range(1, limit + 1):
#     expression = 3 * n ** 2 + 3 * n + 7
#     k = round(expression ** (1 / 3))  # find the nearest integer cube root
#     if k ** 3 == expression:
#         print(f"Found a cube: n={n}, k={k}")

for i in range(1, 101):
    print(pow(i, 3))