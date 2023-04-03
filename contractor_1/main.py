import numpy as np
import csv
import re
import datetime
def catch_time_status():
    time_status = []
    with open("time_status_test") as time_status_file:
        time_status_reader = csv.reader(time_status_file, delimiter=',')
        for row in time_status_reader:
            row[1] = ''.join(str(e) for e in re.findall(r"\d", row[1]))
            time_status.append(row)
        time_status = np.array(time_status)
    return time_status
Min_differ_time = 10*00
Max_groups = 5
time_status = catch_time_status()
time_status.sort()
differ_time = []
for x, y in zip(time_status[:, 0][0::], time_status[:, 0][1::]):
    differ_time.append(int(y)-int(x))
differ_time = np.array(differ_time)
bool_list = [differ_time > Min_differ_time]
print(bool_list)
avilible_time_status = differ_time[bool_list]
avilible_time_status_index = np.argsort(avilible_time_status)[::-Max_groups]
print(avilible_time_status[avilible_time_status_index])
