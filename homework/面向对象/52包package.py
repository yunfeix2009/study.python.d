# 包
# (1) 包的定义
# (2) 包的作用
# (3) 包的导入










# (1) 包的定义
# 包(Package):一个分层次的文件目录结构(简单来说，包就是文件夹)
# 但该文件夹下必须存在__init__.py文件（用于标识当前文件夹是一个python包）
# 该文件的内容可以为空




# (2) 包的作用
# 将有联系的模块放到同一个文件夹下，便于管理和使用模块。






# 课堂练习：
# 新建一个包，名字为package_runoob
# 在新建的包里创建两个文件runoob1.py,runoob2.py




# (3) 导入包
# 包定义好后，需要使用import导入后才能使用


#                                    调用模块里的函数
# import 包名.模块名                 包名.模块名.函数名
# from 包名.模块名 import 函数名      直接用函数名
# from 包名.模块名 import *           直接用函数名
# from 包名 import *                 模块名.函数名

# import package_runoob.runoob1
# import package_runoob.runoob2
# package_runoob.runoob1.runoob1()
# package_runoob.runoob2.runoob2()


# from package_runoob.runoob1 import runoob1
# from package_runoob.runoob2 import runoob2
# runoob1()
# runoob2()


# from package_runoob.runoob1 import *
# from package_runoob.runoob2 import *
# runoob1()
# runoob2()




# from package_runoob import *
# runoob1.runoob1()
# runoob2.runoob2()


# 直接用并不可行
# 需要在__init__.py里用__all__变量来添加模块名来使它可行
# __all__=["runoob1","runoob2"]



# __init__.py文件：控制包的导入
# 为空时仅仅是把这个包导入，不会导入包中的模块

# __all__变量：控制 from 包名 import * 时导入的模块
# 导入包中的模块需要定义__all__变量，
# __all__=["runoob1","runoob2"q]

# from package_runoob import *
# from package_runoob.runoob1 import *
# runoob1.runoob()


# from q0808.h1 import *
# _0808temp_()




# 可以在__init__.py文件中编写语句
# 当导入包时，这些语句就会被执行
# import package_runoob

# 可以在__init__.py文件中编写函数
# 包名.函数名调用

# package_runoob.init_func()



# 课后作业
# 自定义package，练习包的导入，调用这些函数

