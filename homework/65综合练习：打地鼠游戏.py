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

def clear_input():
    wenbenkuang.delete('0.0',tk.END)


def get_remain_count():
    return str(max_count-1)
def hide_da():
    global max_count
    max_count = max_count -1
    if max_count <= 0:
        hit.pack_forget()
        restart_button.pack()

def restart():
    hit.pack()
    init_global_max_count()
    restart_button.pack_forget()

# 初始化
init_global_max_count()

t_tip_input_err=tk.Label(window,text='输入错误:只能输入一到五的数字',font=('字体管家糖果',20), fg='red')
t_tip_input_err.pack_forget()

result=tk.StringVar()
txt = tk.Label(window, textvariable=result)  # 标签的定义，用来显示
txt.pack()

# ”打“的函数
def da_func():
    t_tip_input_err.pack_forget()
    com = ra.randint(1,5)
    hole = wenbenkuang.get('0.0', 'end')
    try:
        hole_people=int(hole.rstrip())
    except:
        t_tip_input_err.pack()
        clear_input()
        return
    if hole_people<1 or hole_people>5:
        clear_input()
        t_tip_input_err.pack()
        return
    if hole_people == com:
        result.set("打中了！\n游戏结束")
        global max_count
        max_count = 0
    else:
        result.set("没打中！\n再试一次吧\n你还有<"+get_remain_count()+">次机会")
    clear_input()
    displayHoleInfo(com-1)
    hide_da()

# 主体代码
for i in range(hole_count):
    var = tk.StringVar()
    var_list.append(var)
    t_list.append( tk.Label(window, textvariable=var) )
    t_list[i].pack()
displayHoleInfo(-1)
t_tip = tk.Label(window, text="请输入您要打那个洞口")  # 标签的定义，用来显示
t_tip.pack()
wenbenkuang = tk.Text(window, height=2.5)
wenbenkuang.pack()
clear=tk.Button(text="清除", command=clear_input)
clear.pack()
hit = tk.Button(text="打")

hit: Button = tk.Button(text="打", command=da_func)  # 设置运行按钮
hit.pack()
restart_button: Button = tk.Button(text="重新开始", command=restart)  # 设置运行按钮

# 显示
window.mainloop()

# 课后作业
# 写一个函数
# 将传入的列表或元组的所有奇数位索引对应的元素，添加到新列表并返回
# 比如，参数是[11,22,33,44,55]，返回[22, 44]
# def func(ob):
#     if type(ob)==type((1,)) or type(ob)==type([1]):
#         ob_ls=list(ob)
#     return ob[1:len(ob_ls):2]
# print(func((21,1,4,45,654,63,4,36436,436,4364,)))