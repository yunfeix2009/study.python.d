# 简易计算器

# tkinter 
# Entry和Button


# 计算器主要分为两个部分：button和显示区
#     button:主要包括0~9、+、-、*、/、C（清除）、=
#     显示区:显示输入和结果的地方
# 所以要先创建一个固定大小的window,
# 在window里创建button并且设置各个buttonn的位置


from tkinter import *


def GetInputValue(ShowNumEntry, Value):  # 用来显示值
    ShowNumEntry.insert(END, Value)

def GetNumOne():  # 按钮1并显示
    GetInputValue(ShowNumEntry, "1")
def GetNumTwo():  # 按钮2并显示
    GetInputValue(ShowNumEntry, "2")
def GetNumThree(): # 按钮3并显示
    GetInputValue(ShowNumEntry, "3")
def GetNumFour():#按钮4并显示
   GetInputValue(ShowNumEntry,"4")
def GetNumFive():#按钮5并显示
   GetInputValue(ShowNumEntry,"5")
def GetNumSix():#按钮6并显示
   GetInputValue(ShowNumEntry,"6")
def GetPoint():#按钮.并显示
    GetInputValue(ShowNumEntry,".")
def GetNumSeven():#按钮7并显示
    GetInputValue(ShowNumEntry,"7")
def GetNumEight():#按钮8并显示
    GetInputValue(ShowNumEntry,"8")
def GetNumNine():#按钮9并显示
    GetInputValue(ShowNumEntry,"9")
def GetNumZero():#按钮0并显示
    GetInputValue(ShowNumEntry,"0")
def GetDot():#按钮.并显示
    GetInputValue(ShowNumEntry,".")
def GetPlus():#按钮+并显示
    GetInputValue(ShowNumEntry,"+")
def GetMinus():#按钮-并显示
    GetInputValue(ShowNumEntry,"-")
def GetClean():#清除
    ShowNumEntry.delete(0,END)
def GetMultiply():#按钮*并显示
    GetInputValue(ShowNumEntry,"*")
def GetDivision():#按钮/并显示
    GetInputValue(ShowNumEntry,"/")
def GetResult():#计算结果并显示
    result = eval(ShowNumEntry.get())
    GetClean()
    ShowNumEntry.insert(0,str(result))


## 创建window      
window = Tk()#创建窗口
window.geometry("420x160")#设置大小

# Entry文本框
ShowNumEntry=Entry(window,width=8,justify="right",font=12 )
ShowNumEntry.grid(row=0,column=5)#布局,row代表行,column代表列,都从0开始

# Button按钮
# command=函数名，可以在按钮被点击时调用相应的函数
NumOneBtn = Button(window,text = "1", width = 8,height = 2,command = GetNumOne)
NumOneBtn.grid(row=1, column=0)
NumTwoBtn = Button(window,text = "2", width = 8,height = 2,command = GetNumTwo)
NumTwoBtn.grid(row=1, column=1)
NumThreeBtn = Button(window,text = "3", width = 8,height = 2,command = GetNumThree)
NumThreeBtn.grid(row=1, column=2)
PlusBtn = Button(window,text = "+", width = 8,height = 2,command = GetPlus)
PlusBtn.grid(row=1, column=3)
MinusBtn = Button(window,text = "-", width = 8,height = 2,command = GetMinus)
MinusBtn.grid(row=1, column=4)
CleanBtn = Button(window,text = "C", width = 8,height = 2,command = GetClean)
CleanBtn.grid(row=1, column=5)
NumFourBtn = Button(window,text = "4", width = 8,height = 2,command = GetNumFour)
NumFourBtn.grid(row=2, column=0)
NumFiveBtn = Button(window,text = "5", width = 8,height = 2,command = GetNumFive)
NumFiveBtn.grid(row=2, column=1)
NumSixBtn = Button(window,text = "6", width = 8,height = 2,command = GetNumSix)
NumSixBtn.grid(row=2, column=2)
NumSixBtn = Button(window,text = ".", width = 8,height = 2,command = GetPoint)
NumSixBtn.grid(row=2, column=3)
MultiplyBtn = Button(window,text = "*", width = 8,height = 2,command = GetMultiply)
MultiplyBtn.grid(row=2, column=4)
ResultBtn = Button(window,text = "=", width = 8, height = 2,background = "green",command=GetResult)
ResultBtn.grid(row=2, column=5)
NumSevenBtn = Button(window,text = "7",width = 8, height = 2, command = GetNumSeven)
NumSevenBtn.grid(row=3, column=0)
NumEightBtn = Button(window,text = "8", width = 8, height = 2, command = GetNumEight)
NumEightBtn.grid(row=3, column=1)
NumNineBtn = Button(window,text = "9", width = 8, height = 2, command = GetNumNine)
NumNineBtn.grid(row=3, column=2)
NumZeroBtn = Button(window,text = "0", width = 8, height = 2, command = GetNumZero)
NumZeroBtn.grid(row=3, column=3)
DivisionBtn = Button(window,text = "/", width = 8, height = 2, command = GetDivision)
DivisionBtn.grid(row=3, column=4)

window.mainloop()#主循环,窗口显示出来等待各种消息



# 课后作业
# from tkinter import *# 导入 Tkinter 库
# window = Tk() # 创建窗口对象
# # 创建两个列表
# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
# listb  = Listbox(window)# 创建两个列表组件
# listb2 = Listbox(window)
# for item in li:# 第一个小部件插入数据
#     listb.insert(0,item)
# for item in movie:# 第二个小部件插入数据
#     listb2.insert(0,item)
# listb.pack() # 将小部件放置到主窗口中
# listb2.pack()
# window.mainloop()# 进入消息循环