# 有些时候，需要对文件进行重命名、删除等一些操作，
# python的os标准库中都有这些功能


# rename()
# remove()
# mkdir()
# rmdir()
# getcwd()






# rename() 文件或文件夹的重命名
# rename(旧文件(夹)名, 新文件(夹)名)
import os
# os.rename("test1.txt", "test2.txt")
# os.rename("test1", "test2")


# remove() 文件的删除
# remove(待删除的文件名)
import os
# os.remove("test copy.txt")



# mkdir() 创建文件夹（make directory）
# mkdir(新文件夹名称)
# import os
# os.mkdir("张三")


# rmdir() 删除文件夹
# rmdir(要删除的文件夹名称)
# import os
# os.rmdir("test2")


# getcwd() 获取当前工作路径 current working directory
import os
# path = os.getcwd()
# print(path)


# listdir()  获取指定路径下的所有文件和文件夹的名称,返回一个字符串列表
# listdir(文件目录)
import os
# mylist = os.listdir("D:")
# mylist = os.listdir("C:\Program Files")
# mylist = os.listdir()#无参数表示当前目录
# print(mylist)




# 课后作业
# 列出某个目录下的所有以.py结尾的文件名称
import os
fileNames=os.listdir()




i= len(fileNames) - 1
while i>=0:
    name=fileNames[i]
    if not name.endswith('.py'):
        fileNames.remove(name)
    i=i-1
print(fileNames)