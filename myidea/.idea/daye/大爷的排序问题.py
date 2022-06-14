import time



filename = '排序结果.txt'
day_list =  [',A,B,C,D',
            ',E,F,G,H',
            ',I,A,B,C',
            ',D,E,F,G',
            ',H,I,A,B',
            ',C,D,E,F',
            ',G,H,I,A',
            ',B,C,D,E',
            ',F,G,H,I']
last_list = ''



time_a = int(input('输入时间（天）'))



time.strftime('%A')
index = int(time.strftime('%w'))
nowtime = time.time()



for i in range(1,time_a+1):
    if (i-1 + index) % 7==0:
        x = 7
    else:
        x=(i-1 + index) % 7
    last_list = last_list + time.strftime('%Y-%m-%d',time.localtime(nowtime + (i-1)*86400 )) + ',' + str(x) + day_list[(i - 1) % 9] + '\n'



filename = '排序结果.txt'
with open(filename, 'w',encoding='UTF-8') as file_object:
    file_object.write('日期,周,一厂上午,一厂下午,二厂上午,二厂下午' '\n')
    file_object.write(last_list)