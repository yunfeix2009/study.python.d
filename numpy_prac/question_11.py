def sum_digit(n):
    str_n = str(n)
    sum = str_n[0]
    sum_2 = str_n[1]
    sum_3 = str_n[2]
    sum_4 = str_n[3]
    return int(sum)+int(sum_2)+int(sum_3)+int(sum_4)
print(sum_digit(2023))
for i in range(2023, 10000):
    if i-(23*sum_digit(i)) == 2023:
        print(i)