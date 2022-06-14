import turtle as t

#位移函数
def Skip(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# 绘制五星红旗
def draw(t,x,y,z):
    t.begin_fill()
    for i in range(x):
        t.forward(y)
        t.left(z)
    t.end_fill()

"""画笔基础设置"""
t.screensize(1200,800)
t.pensize(5)
t.hideturtle()
t.speed(5)
t.pencolor("red")

# 画笔移动
Skip(t,0,-200)

# 绘制国旗
t.fillcolor("red")
t.begin_fill()
t.forward(300)
t.left(90)
t.forward(400)
t.left(90)
t.forward(600)
t.left(90)
t.forward(400)
t.left(90)
t.forward(300)
t.end_fill()

# 画笔移动
Skip(t,-250,115)

# 绘制大五角星
t.pencolor("yellow")
t.fillcolor("yellow")

t.begin_fill()
for i in range(5):
  t.forward(100)
  t.right(144)
t.end_fill()

"""第一颗副星"""
# 画笔移动
Skip(t,-120,10)
# 绘制小五星
draw(t,5,30,144)


"""第二颗副星"""
# 画笔移动
Skip(t,-80,50)
# 绘制小五星
draw(t,5,30,144)

"""第三颗副星"""
# 画笔移动
Skip(t,-80,110)
# 绘制小五星
draw(t,5,30,144)

"""第四颗副星"""
# 画笔移动
Skip(t,-120,150)
# 绘制小五星
draw(t,5,30,144)
t.done()
