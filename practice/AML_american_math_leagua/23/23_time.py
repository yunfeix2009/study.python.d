import time as t
t_s=t.time()
i=6210001000
if str(str(i).count('0')) + str(str(i).count('1')) + str(str(i).count('2')) + str(str(i).count('3')) + str(
        str(i).count('4')) + str(str(i).count('5')) + str(str(i).count('6')) + str(str(i).count('7')) + str(
        str(i).count('8')) + str(str(i).count('9')) == str(i):
    print(i)
t_f=t.time()
print((t_f-t_s)*100000)