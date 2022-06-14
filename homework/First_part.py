from tkinter import *
import first_part_baidutransapi


def exec_trans():
    q = entry1.get()
    dst = first_part_baidutransapi.trans(q)
    res.set(dst)

# 创建窗口
root = Tk()
# 标题
root.title("汉译英")
# 窗口大小
root.geometry("370x100")
# 获取屏幕宽
screen_width = root.winfo_screenwidth()
# 获取屏幕高度
screen_height = root.winfo_screenheight()
x_ = (screen_width - 370) // 2
y_ = (screen_height - 100) // 2
# 计算页面打开在屏幕中央的位置
root.geometry("+{}+{}".format(x_, y_))
# 第一列标签
label1 = Label(root,text="输入中文:")
# 定位布局 grid网格式布局 pack包 place位置
label1.grid(row=0,column=0)
# 输入控件
entry1 = Entry(root, font=("微软雅黑", 15))
entry1.grid(row=0,column=1)


# 翻译结果标签
label2 = Label(root,text="翻译结果:")
label2.grid(row=1,column=0)
# 翻译结果输入框
res = StringVar()
entry2 = Entry(root, font=("微软雅黑", 15), textvariable=res)
entry2.grid(row=1,column=1)
# 按钮
button1 = Button(root,text="翻译",width=10,command=exec_trans)
# sticky 对齐方式 N S W E 上下左右
button1.grid(row=2,column=0,sticky=W)
# 退出按钮 command是点击事件的方法
button2 = Button(root,text="离开",width=10,command=root.quit)
button2.grid(row=2,column=1,sticky=E)
# 显示窗口 消息循环 接收对窗口的所有操作的消息
root.mainloop()

