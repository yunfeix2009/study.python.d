import os
def os_findfile(name,list):
    for i in os.listdir(name):
        child_path = os.path.join(name, i)
        if os.path.isdir(child_path):
            os_findfile(child_path,list)
        else:
            list.append(child_path)
    return list
print(os_findfile('D:\dev\projs\homework\os_dir',[]))