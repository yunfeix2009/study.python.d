import tkinter as tk
window = tk.Tk()
window.title('打地鼠 ')
window.geometry('800x600')
def print_shengrikuaile():
    t_tip = tk.Label(window, text="大爷生日快乐",font=('字体管家糖果',50), fg='blue')  # 标签的定义，用来显示
    t_tip.pack()
Button = tk.Button(text="点我", command=print_shengrikuaile)  # 设置运行按钮
Button.pack()
tk.mainloop()