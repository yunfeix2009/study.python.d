# 石头剪刀布

# 图形化界面库 tkinter
    # 窗口
        # Tk()#创建窗口
        # mainloop() #主循环,窗口显示出来等待各种消息
        # title() # 设置窗口名字
        # geometry('300x300') # 设置窗口大小
    # 窗口有以下组件：
        # Text 文本框   用来输入。可以多行
            # Text()创建文本框
        # Button 按钮   用来点击
        # Label 标签    用来显示
    # 组件加入窗口
        # pack()包装

import random
import tkinter as tk

def panduan():
    suiji = ['石头','剪刀','布'] # 定义列表
    computer = random.choice(suiji) # 从列表中随机选出一个手势
    shuru = wenbenkuang.get("0.0", "end")  # 获取第0行第0列，代表用户输入的手势
    yonghu = shuru.rstrip() # 获取到的手势后有一个空行，将空行去掉
    t['text'] = "你输入的是：%s\n电脑输入的是：%s\n"%(yonghu,computer)
    if yonghu == computer:
        t['text'] +="平局"
    elif (computer == "石头" and yonghu == "剪刀") or (computer =="剪刀" and yonghu == "布")\
            or (computer== "布" and yonghu == "石头"):
        t['text'] +="你输了"
    elif (computer == "石头" and yonghu == "布") or (computer =="剪刀" and yonghu == "石头")\
            or (computer== "布" and yonghu == "剪刀"):
        t['text'] +="你赢了"
    else:
        t['text'] = "输入错误！请重新输入"

window=tk.TK() # 定义窗口
window.title('石头剪刀布') # 设置窗口名字
window.geometry('300x300') # 窗口大小
wenbenkuang = tk.Text(window,height=2) # 文本框的定义
wenbenkuang.pack()# 组件加入窗口

run = tk.Button(text="运行",command=panduan) # 设置运行按钮
run.pack()

t=tk.Label(window, text = "开始") # 标签的定义，用来显示
t.pack()
window.mainloop()
