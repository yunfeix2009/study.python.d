# 学生管理系统
# 系统介绍
# 该系统主要是为了保存学生信息(主要包括学生姓名、学生手机号及QQ号)
# 我们可以通过系统完成以下功能
# 1新增学生信息(输入学生姓名、学生手机号及QQ号)
# 2删除学生信息(输入要删除的学生索引)
# 3修改学生信息(输入要修改的学生索引，学生姓名、学生手机号及QQ号)
# 4查询学生信息(输入学生姓名)
# 5显示所有学生信息、
# 6退出系统
info_list = [{"name": "xiaoming", "mobilephone": 123456, "qq": 1234},
             {"name": "xiaohong", "mobilephone": 33121, "qq": 124, }]
# 显示系统界面


def print_menu():
    print("学生管理系统V1．0")
    print("1：添加学生")
    print("2：删除学生")
    print("3：修改学生")
    print("4：查询学生")
    print("5．显示所有学生")
    print("6：退出系统")


# 定一个列表，用来存储所有的学生信息(每个学生是一个字典),
# 考虑到增删改都要操作这个列表，我们把它定义为全局的列表

def print_all_info() :
    print(info_list)
def search_info():
    name=input('请输入要查询的姓名。')
    print(findByName(name,info_list))
def findByName(name:str,list:list):
    for dict in list:
        if dict['name']==name:
            return dict
def add_new_info():
    dict={'name':'','mobilephone':'','qq':''}
    name=input('姓名是？')
    dict['name']=name
    while True:
        try:
            mobilephone=int(input('手机号是？'))
            break
        except:
            print('输入错误，请输入数字。')
    dict['mobilephone'] = mobilephone
    while True:
        try:
            qq = int(input('QQ号是？'))
            break
        except:
            print('输入错误，请输入数字。')
    dict['qq'] = qq
    info_list.append(dict)
    print('这是添加好的')
    print(info_list)
def del_info():
    del_name=input('请输入要删除学生的姓名')
    if del_name in info_list:
        flag=input('是否删除？(yes or no)')
        if flag=='yes':
            info_list.remove(findByName(del_name,info_list))
            print('删除成功')
        elif flag=='no':
            pass
        else:
            print('输入错误，默认跳过。')
    else:
        print('输入错误,没有此学生，默认跳过。')
def modify_info():
    modify_name=input('请输入要修改的姓名')
    dict=findByName(modify_name,info_list)
    while True:
        try:
            modify = int(input('你要修改qq号还是手机号（qq号为1，手机号为2）'))
            break
        except:
            print('输入错误，请输入数字。')
    modify=int(modify)
    if modify==1:
        while True:
            try:
                modify_what=int(input('修改成什么'))
                break
            except:
                print('输入错误，请输入数字。')
        dict['qq']=modify_what
    elif modify==2:
        while True:
            try:
                modify_what = int(input('修改成什么'))
                break
            except:
                print('输入错误，请输入数字。')
        dict['mobilephone'] = modify_what
    print(info_list)

from.二分查找 import *
from _module_ import *
def all_process():
    haha()
    print(find_2222([12,414325,14523,6,6,235,7,57,264,26,257,536,2356,6274,37,3],6))
    while True:#用来控制整个流程
        print_menu()#1:打印功能
        num=input("请输入要进行的操作(数字)：")#2:获取用户的选择
        #3:根据用户选择，做相应的事情
        if num=="1":#添加学生
            add_new_info()
        elif num=="2":#删除学生
            del_info()
        elif num=="3":#修改学生
            modify_info()
        elif num=="4":#查询学生
            search_info()
        elif num=="5":#显示所有的信息
            print_all_info()
        elif num=="6":#退出系统
            exit_flag=input("亲，你确定要退出么?(yes or no)")
            if exit_flag=="yes":
                print("退出成功")
                break
        else:
            print("输入有误，请重新输入......")
