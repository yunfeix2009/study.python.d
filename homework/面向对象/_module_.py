# 模块
# 1模块的定义
# 2模块的作用
# 3模块的导入










# (1) 模块的定义
# Python模块(Module)：一个以.py结尾的Python文件


# 模块里能定义：函数、变量，可执行的代码
# 例如：我们新建一个support.py文件



# (2) 模块的作用：
# 有逻辑地组织Python代码
# 把相关的代码放到一个模块里，让代码更好用，更易懂。




# (3) 模块的引入
# 模块定义好后，需要用import导入后才能使用
# 不管执行了多少次import,一个模块只会被导入一次

#                                              调用函数
# import 模块名             导入模块            模块名.函数名
# from 模块名 import *      从模块导入所有函数   直接用函数名
# from 模块名 import 函数名  从模块导入一个函数   直接用函数名


# import support
# support.print_func()

# from support import *
# print_func()

# from support import add_func
# res = add_func(1,2)
# print(res)
# print_func()


# 课后作业
# 自定义一个support.py文件，在support.py文件里定义函数，
# 练习模块的导入，并调用这些函数

# from 面向对象.学生管理系统 import *
# def daoru():
#     all_process()
# daoru()
#
#
# def haha():
#     print("hahaha")