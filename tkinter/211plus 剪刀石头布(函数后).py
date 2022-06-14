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

# def panduan():
#     suiji = ['石头','剪刀','布'] # 定义列表
#     computer = random.choice(suiji) # 从列表中随机选出一个手势
#     shuru = wenbenkuang.get("0.0", "end")  # 获取第0行第0列，代表用户输入的手势
#     yonghu = shuru.rstrip() # 获取到的手势后有一个空行，将空行去掉
#     t_2['text'] = "你输入的是：%s\n电脑输入的是：%s\n"%(yonghu,computer)
#     if yonghu == computer:
#         t_2['text'] +="平局"
#     elif (computer == "石头" and yonghu == "剪刀") or (computer =="剪刀" and yonghu == "布")\
#             or (computer== "布" and yonghu == "石头"):
#         t_2['text'] +="你输了"
#     elif (computer == "石头" and yonghu == "布") or (computer =="剪刀" and yonghu == "石头")\
#             or (computer== "布" and yonghu == "剪刀"):
#         t_2['text'] +="你赢了"
#     else:
#         t_2['text'] = "输入错误！请重新输入"
#
# window=tk.Tk() # 定义窗口
# window.title('石头剪刀布') # 设置窗口名字
# window.geometry('300x300') # 窗口大小
# wenbenkuang = tk.Text(window,height=2) # 文本框的定义
# wenbenkuang.pack()# 组件加入窗口
#
# run = tk.Button(text="运行",command=panduan) # 设置运行按钮
# run.pack()
#
# t_2=tk.Label(window, text = "开始") # 标签的定义，用来显示
# t_2.pack()
# window.mainloop()


# 课后作业
# 将以下功能用tkinter库做成图形化界面

# 输入一个人的身高(m)和体重(kg)
# 根据BMI公式计算他的BMI指数并输出对应的结果(BMI=体重÷身高的平方)
# 例如：一个人52kg,身高1.55m,则BMI=52/(1.55*1.55)= 21.6，输出正常
# BMI指数:      结果:

# BMI<=18.5：    过轻
# 18.5<BMI<=25： 正常
# 25<BMI<=28：   过重
# 28<BMI<=32：   肥胖
# BMI>32：      严重肥胖

import tkinter as tk
def BMI():
    h_1=wenbenkuang_1.get('0.0','end')
    h = h_1.rstrip()
    w_1=wenbenkuang_2.get('0.0','end')
    w = w_1.rstrip()
    bmi=(float(w)/float(h))/float(h)
    if bmi<=18.5:
        t = tk.Label(window, text='过轻')  # 标签的定义，用来显示
        # t.pack()
    elif bmi<=18.5:
        t = tk.Label(window, text='正常')  # 标签的定义，用来显示
        # t.pack()
    elif bmi<=32:
        t = tk.Label(window, text='过重')  # 标签的定义，用来显示
        # t.pack()
    elif bmi<=25:
        t = tk.Label(window, text='肥胖')  # 标签的定义，用来显示
        # t.pack()
    elif bmi<=25:
        t = tk.Label(window, text='严重肥胖')  # 标签的定义，用来显示
    t.pack()
    t = tk.Label(window, text=bmi)  # 标签的定义，用来显示
    t.pack()
window=tk.Tk()
window.title('体重计')
window.geometry('250x250')
t_1=tk.Label(window, text = "请输入您的身高(m)") # 标签的定义，用来显示
t_1.pack()
wenbenkuang_1=tk.Text(window,height=2.5)
wenbenkuang_1.pack()
t_2=tk.Label(window, text ="请输入您的体重(kg)") # 标签的定义，用来显示
t_2.pack()
wenbenkuang_2=tk.Text(window,height=2.5)
wenbenkuang_2.pack()
run = tk.Button(text="运行",command=BMI) # 设置运行按钮
run.pack()

window.mainloop()