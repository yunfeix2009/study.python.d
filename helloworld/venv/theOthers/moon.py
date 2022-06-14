import turtle as t

t.screensize(800, 600, "#483d8b")  # 画布尺寸和颜色
t.up()  # 抬起笔
t.goto(-100, 64)  # 把笔移到坐标的位置
t.pd()  # 放下笔
t.fillcolor('#ffd700')  # 填充色
t.begin_fill()  # 开始填充（一定要在画你想画的图案之前）
t.pencolor('#ffd700')  # 画笔颜色
t.pensize(3)  # 画笔尺寸
t.circle(18)  # 圆的半径
t.end_fill()  # 结束填充（在画完之后）

t.up()
t.goto(-110, 60)
t.pd()
t.pencolor('#ff0000')
t.pensize(10)
t.fd(20)

t.up()
t.goto(-120, 60)
t.pd()
t.pencolor('#ff0000')
t.pensize(10)
t.seth(-40)  # 画笔移动方向
for i in range(3):
    t.circle(40, 80)
t.circle(-40, 80)
t.circle(40, 80 / 2)

t.up()
t.goto(-100, 34)
t.pd()
t.pensize(55)
t.pencolor('#adff2f')
t.seth(-90)
t.fd(36)
t.seth(7)
t.pensize(8)
t.pencolor("yellow")
t.fillcolor('yellow')
t.speed(15)  # 速度
t.begin_fill()
t.circle(-800)
t.end_fill()

t.pencolor('#ffd700')
t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(200, -300)
t.pd()
t.pensize(5)
t.circle(20)
t.end_fill()

t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(500, -300)
t.pd()
t.pensize(6)
t.circle(50)
t.end_fill()

t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(-200, -300)
t.pd()
t.pensize(6)
t.circle(35)
t.end_fill()

t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(-100, -200)
t.pd()
t.pensize(6)
t.circle(44)
t.end_fill()

t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(-300, -200)
t.pd()
t.pensize(6)
t.circle(34)
t.end_fill()

t.up()
t.fillcolor('#daa520')
t.begin_fill()

t.goto(-350, -350)
t.pd()
t.pensize(6)
t.circle(20)
t.end_fill()

t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(-350, -350)
t.pd()
t.pensize(6)
t.circle(20)
t.end_fill()

t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(100, -350)
t.pd()
t.pensize(6)
t.circle(30)
t.end_fill()

t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(-500, -350)
t.pd()
t.pensize(6)
t.circle(50)
t.end_fill()

t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(200, -200)
t.pd()
t.pensize(6)
t.circle(60)
t.end_fill()

t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(360, -360)
t.pd()
t.pensize(6)
t.circle(70)

t.end_fill()
t.up()
t.fillcolor('#daa520')
t.begin_fill()
t.goto(50, -100)
t.pd()
t.pensize(6)
t.circle(50)
t.end_fill()

t.done()