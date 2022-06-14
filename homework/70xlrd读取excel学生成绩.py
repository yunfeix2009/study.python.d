# 读取excel学生成绩表

# 1读取Excel学生成绩表的数据,转换为python数据类型的数据
# 2输出每个学生的成绩平均分
# 3输出python成绩大于80分的学生姓名及对应的python成绩
# 4输出有满分科目的学生姓名及对应的满分科目


# xlrd 读取excel的python第三方库
import xlrd#导入xlrd
data=xlrd.open_workbook('student(1).xls')#打开xls文件
table=data.sheets()[0]#打开第一张表
nrows=table.nrows#获取表的行数
stu_score_list = []
for i in range(nrows):#循环逐行打印
    if i==0:
        continue
    print(table.row_values(i))
    stu_score_list.append(table.row_values(i))
for i in range(1,nrows):
    print([table.row_values(i), (int(table.row_values(i)[1])+int(table.row_values(i)[2])+int(table.row_values(i)[3])+int(table.row_values(i)[4])+int(table.row_values(i)[5]))/5])
for i in range(1,nrows):
    if int(table.row_values(i)[5])>=80:
        print([table.row_values(i)[0],int(table.row_values(i)[5])])
for i in range(1,nrows):
    for j in range(1,len(table.row_values(i))):
        if j==100:
            print(table.row_values(i)[0],table.row_values(0)[j])







# 课后作业
# 把str1,list1,tuple1,dict1写入到同一个文件中
# str1='abcde'
# list1=[1,3,5,7,9]
# tuple1=('red','blue','yellow')
# dict1={'a':1,'b':2,'c':3}
