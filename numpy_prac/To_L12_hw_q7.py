ls = []
ls_2 = []
for i in range(1000, 10000):
    thousandth = int(str(i)[0])
    hundredth = int(str(i)[1])
    tenth = int(str(i)[2])
    digit = int(str(i)[3])
    if digit>thousandth>hundredth>tenth:
        ls.append(i)
for i in range(1000, 10000):
    thousandth = int(str(i)[0])
    hundredth = int(str(i)[1])
    tenth = int(str(i)[2])
    digit = int(str(i)[3])
    if thousandth>hundredth>tenth>digit:
        ls_2.append(i)
print(len(ls))
print(len(ls_2))

print(ls)
print(ls_2)