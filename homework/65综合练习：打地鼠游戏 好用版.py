# 综合练习：打地鼠游戏

# 编写代码模拟打地鼠游戏
# 1·假设共有五个洞口，老鼠在里面随机一个洞口
# 2·人随机打开一个洞口，如果有老鼠，代表抓到了
# 3·如果没有，继续打地鼠,但是地鼠会跳到其他洞口。

# 用随机数模拟地鼠在哪个洞口
# 有五个洞口，所以可以随机产生1-5这五个随机整数。
# 1代表地鼠在第一个洞口
# 2代表地鼠在第二个洞口
# ...

# 通过让用户输入模拟打地鼠，
# 用户输入1-5的整数，代表要打哪个地鼠洞口
# 如果输入的数字和随机产生的数字相等，就代表打到地鼠了(程序结束)
# # 否则继续输入数字模拟打地鼠(一共五次机会)

import random as ra
import tkinter as tk
from tkinter import Button

# 创建窗口
window = tk.Tk()
window.title('打地鼠 ')
window.geometry('800x600')
hole_count = 5

# 洞口可视化
t_list = []
var_list = []
b_list=[]
# 定义函数
def init_global_max_count():
    global max_count
    max_count = 5

def displayHoleInfo( mouse_in_hole:int ):
    for i in range(hole_count):
        if mouse_in_hole==i :
            var_list[i].set( "洞["+str(i+1)+"] -- 里有老鼠！")
        else:
            var_list[i].set("洞["+str(i+1)+"]")

def get_remain_count():
    return str(max_count-1)

def hide_da():
    global max_count
    max_count = max_count -1
    if max_count <= 0:
        for i in range(hole_count):
            # t_list[i].pack_forget()
            b_list[i]['state']='disabled'
        restart_button.pack()

def restart():
    for i in range(hole_count):
        # t_list[i].pack()
        b_list[i]['state']='normal'
    init_global_max_count()
    restart_button.pack_forget()
    displayHoleInfo(-1)

# 初始化
init_global_max_count()


result=tk.StringVar()
txt = tk.Label(window, textvariable=result)  # 标签的定义，用来显示
txt.pack()

# ”打“的函数
def da_func(num):
    com = ra.randint(1,5)
    hole_people = num
    if hole_people == com:
        result.set("打中了！\n游戏结束")
        global max_count
        max_count = 0
    else:
        result.set("没打中！\n再试一次吧\n你还有<"+get_remain_count()+">次机会")
    displayHoleInfo(com-1)
    hide_da()

# 主体代码
for i in range(hole_count):
    var = tk.StringVar()
    var_list.append(var)
    t_list.append( tk.Label(window, textvariable=" ") )
    b_list.append(tk.Button(text="洞口"+str(i+1),width=40,height=2, textvariable=var))
    t_list[i].pack()
    b_list[i].pack()
b_list[0]['command']=lambda : da_func(1)
b_list[1]['command']=lambda : da_func(2)
b_list[2]['command']=lambda : da_func(3)
b_list[3]['command']=lambda : da_func(4)
b_list[4]['command']=lambda : da_func(5)


displayHoleInfo(-1)
t_tip = tk.Label(window, text="请点击您要打的那个洞口")  # 标签的定义，用来显示
t_tip.pack()



restart_button: Button = tk.Button(text="重新开始", command=restart)  # 设置运行按钮

# 显示
window.mainloop()

# 课后作业
# 写一个函数
# 将传入的列表或元组的所有奇数位索引对应的元素，添加到新列表并返回
# 比如，参数是[11,22,33,44,55]，返回[22, 44]
