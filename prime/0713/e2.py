# 判断年份是否是闰年
year=int(input('请输入年份。'))
if year%400==0 or year%4==0 and not year%100==0:
    print('是闰年')
else:
    print('不是润年20')