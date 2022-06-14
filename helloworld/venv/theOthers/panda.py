import turtle as t
# 设置初始画布和画笔
t.setup(width=1450, height=1450, startx=0, starty=0)
t.speed(0)
t.rt(-120)
t.up()
t.pensize(6)
t.goto(180, 150)
t.bgcolor('white')
t.title("My Panda")
t.down()
t.color('black')
#头轮廓
t.circle(190, 100)
t.fd(20)
for i in range(260):
    t.fd(1)
    t.lt(0.5)
for i in range(8):
    t.fd(19)
    t.lt(1)
for i in range(260):
    t.fd(1)
    t.lt(0.5)
t.up()
#身子轮廓
t.goto(-70, -16)
t.setheading(245)
t.down()
for i in range(35):
    t.fd(1.5)
    t.lt(0.5)
for i in range(5):
    t.fd(1.5)
    t.lt(0.0125)
for i in range(9):
    t.fd(0.75)
    t.lt(1.5)
for i in range(22):
    t.fd(1)
    t.lt(0.3)
for i in range(20):
    t.fd(1)
    t.lt(3)
for i in range(180):
    t.fd(1)
    t.lt(0.20)
for i in range(20):
    t.fd(1)
    t.lt(3)
for i in range(22):
    t.fd(1)
    t.lt(0.3)
for i in range(9):
    t.fd(0.75)
    t.lt(1.5)
for i in range(5):
    t.fd(1.5)
    t.lt(0.0125)
for i in range(25):
    t.fd(1.5)
    t.lt(0.5)
t.up()
#脚
#右脚
t.goto(-65, -119)
t.down()
t.begin_fill()
t.color('black')
t.setheading(280)
t.circle(30, 135)
t.end_fill()
t.up()
#左脚
t.goto(50, -129)
t.down()
t.begin_fill()
t.color('black')
t.setheading(305)
t.circle(30, 135)
t.end_fill()
t.up()
#耳朵
#左耳
t.goto(200, 118)
t.down()
t.begin_fill()
t.color('black')
t.setheading(20)
t.circle(50, 210)
t.end_fill()
t.up()
#右耳
t.goto(-70, 227)
t.down()
t.begin_fill()
t.color('black')
t.setheading(103)
t.circle(50, 230)
t.end_fill()
t.up()
t.goto(117, -40)
t.setheading(25)
t.down()
#手
#左手
t.begin_fill()
t.color('black')
for i in range(70):
    t.fd(1)
    t.lt(-0.5)
for i in range(160):
    t.fd(0.25)
    t.lt(-0.9)
for i in range(70):
    t.fd(1)
    t.lt(-0.65)
t.end_fill()
t.up()
#右手
t.goto(-75, -25)
t.setheading(155)
t.down()
t.begin_fill()
t.color('black')
for i in range(70):
    t.fd(1)
    t.lt(0.5)
for i in range(160):
    t.fd(0.25)
    t.lt(0.85)
for i in range(70):
    t.fd(1)
    t.lt(0.65)
t.end_fill()
#眼睛
#右眼
t.up()
t.goto(-45, 80)
t.begin_fill()
t.color('black')
t.down()
t.circle(25.25)
t.end_fill()
t.up()
t.goto(-50.5, 74.5)
t.begin_fill()
t.color('black')
t.down()
t.circle(26.25)
t.end_fill()
t.up()
t.goto(-43, 100)
t.begin_fill()
t.color('white')
t.down()
t.circle(5.5)
t.end_fill()
t.up()
#左眼
t.goto(100, 67)
t.begin_fill()
t.color('black')
t.down()
t.circle(25.25)
t.end_fill()
t.up()
t.goto(105.5, 63.5)
t.begin_fill()
t.color('black')
t.down()
t.circle(25.25)
t.end_fill()
t.up()
t.goto(96, 92)
t.begin_fill()
t.color('white')
t.down()
t.circle(5.5)
t.end_fill()
t.up()
#腮红
#左
t.goto(105, 40)
t.begin_fill()
t.color('tomato')
a = 0.45
t.down()
t.setheading(270)
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a+0.045
        t.lt(3)
        t.fd(a)
    else:
        a = a-0.045
        t.lt(3)
        t.fd(a)
t.end_fill()
t.up()
#右
t.goto(-60, 50)
t.begin_fill()
t.color('tomato')
a = 0.4
t.down()
t.setheading(90)
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a+0.04
        t.lt(3)
        t.fd(a)
    else:
        a = a-0.04
        t.lt(3)
        t.fd(a)
t.end_fill()
t.up()
#鼻子
t.goto(20, 75)
t.begin_fill()
t.color('black')
t.setheading(125)
t.down()
for i in range(25):
    t.fd(0.75)
    t.lt(-1)
for i in range(20):
    t.fd(0.25)
    t.lt(-4.5)
for i in range(30):
    t.fd(0.75)
    t.lt(-1)
for i in range(20):
    t.fd(0.25)
    t.lt(-4.5)
for i in range(25):
    t.fd(0.75)
    t.lt(-1)
for i in range(20):
    t.fd(0.25)
    t.lt(-4.5)
t.end_fill()
t.up()
#嘴巴
t.setheading(260)
t.goto(23, 75)
t.down()
for i in range(45):
    t.fd(1)
    t.lt(3)
t.up()
t.setheading(260)
t.goto(23, 75)
t.down()
for i in range(45):
    t.fd(1)
    t.lt(-3)
#字
t.color('red')
x = -100
t.up()
t.goto(x, 300)
t.down()
t.write('I', align='center', font=('Arial', 30, 'bold'))
t.up()
t.color('orange')
x = x + 25
t.goto(x, 300)
t.down()
t.write('l', align='center', font=('Arial', 30, 'bold'))
t.up()
x = x + 13
t.color('gold')
t.goto(x, 300)
t.down()
t.write('o', align='center', font=('Arial', 30, 'bold'))
t.up()
t.color('green')
x = x + 15
t.goto(x, 300)
t.down()
t.write('v', align='center', font=('Arial', 30, 'bold'))
t.up()
t.color('lime')
x = x + 15
t.goto(x, 300)
t.down()
t.write('e', align='center', font=('Arial', 30, 'bold'))
t.up()
t.color('blue')
x = x + 30
t.goto(x, 300)
t.down()
t.write('m', align='center', font=('Arial', 30, 'bold'))
t.up()
x = x + 20
t.color('purple')
t.goto(x, 300)
t.down()
t.write('y', align='center', font=('Arial', 30, 'bold'))
t.up()
t.color('black')
x = x + 30
t.goto(x, 300)
t.down()
t.write('P', align='center', font=('Arial', 30, 'bold'))
t.up()
t.color('grey')
x = x + 17
t.goto(x, 300)
t.down()
t.write('a', align='center', font=('Arial', 30, 'bold'))
t.up()
t.color('black')
x = x + 17
t.goto(x, 300)
t.down()
t.write('n', align='center', font=('Arial', 30, 'bold'))
t.up()
t.color('grey')
x = x + 17
t.goto(x, 300)
t.down()
t.write('d', align='center', font=('Arial', 30, 'bold'))
t.up()
t.color('black')
x = x + 17
t.goto(x, 300)
t.down()
t.write('a', align='center', font=('Arial', 30, 'bold'))
t.ht()
#结束
t.done()