import numpy as np

def generate_arrangements(arr, n):
    if n == 0:
        try:
            arr = arr.reshape((3, 3))
            if (arr[0, 0] - arr[0, 1] + arr[0, 2] == 0 or arr[0, 0] - arr[0, 1] + arr[0, 2] == 11) \
                and (arr[1, 0] - arr[1, 1] + arr[1, 2] == 0 or arr[1, 0] - arr[1, 1] + arr[1, 2] == 11) \
                and (arr[2, 0] - arr[2, 1] + arr[2, 2] == 0 or arr[2, 0] - arr[2, 1] + arr[2, 2] == 11) \
                and (arr[0, 1] - arr[1, 1] + arr[2, 1] == 0 or arr[0, 1] - arr[1, 1] + arr[2, 1] == 11) \
                and (arr[0, 2] - arr[1, 2] + arr[2, 2] == 0 or arr[0, 2] - arr[1, 2] + arr[2, 2] == 11) \
                and (arr[0, 0] - arr[1, 1] + arr[2, 2] == 0 or arr[0, 0] - arr[1, 1] + arr[2, 2] == 11):
                return arr.tolist()
        except ValueError:
            pass
    else:
        arrangements = []
        for i in range(1, 10):
            if i not in arr:
                new_arr = np.append(arr, i)
                sub_arrangements = generate_arrangements(new_arr, n - 1)
                if sub_arrangements is not None:
                    arrangements += sub_arrangements
        return arrangements

arrangements = generate_arrangements(np.array([], dtype=np.int64), 9)
print(np.array(arrangements))
