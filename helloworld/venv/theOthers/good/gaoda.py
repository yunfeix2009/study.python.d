import turtle
t=turtle.Turtle()
turtle.Turtle().screen.delay(0)
tleft=turtle.Turtle()
#第一部分
t.penup()
t.goto(0,0)
t.pendown()
t.left(20)
t.forward(110)
t.left(25)
t.forward(40)
t.left(100)
t.circle(180,20)
t.right(120)
t.forward(250)
t.left(165)
t.forward(250)
t.right(100)
t.forward(35)
t.left(70)
t.forward(45)
t.left(70)
t.forward(120)
t.left(70)
t.forward(80)
t.left(80)
t.forward(80)
t.left(68)
t.forward(120)
t.left(180)
t.forward(78)
t.right(68)
t.forward(60)
t.right(75)
t.forward(60)
t.right(110)
t.forward(15)
t.left(38)
t.forward(65)
t.right(73)#五边形的直边
t.forward(35)
t.right(70)
t.forward(65)
t.right(68)
t.forward(50)
t.right(80)
t.forward(50)
t.penup()
t.goto(-65,68)
t.pendown()
t.right(7)
t.forward(350)
t.right(165)
t.forward(330)
t.penup()
t.goto(64,65)
t.pendown()
t.left(75)
t.forward(350)
t.left(165)
t.forward(330)
t.penup()
t.goto(300,500)
#第二部分
tleft.left(180)
tleft.right(20)
tleft.forward(110)
tleft.right(25)
tleft.forward(40)
tleft.right(100)
tleft.circle(-180,20)
tleft.left(120)
tleft.forward(250)
tleft.right(165)
tleft.forward(250)
tleft.left(100)
tleft.forward(35)
tleft.penup()
tleft.goto(0,0)
tleft.pendown()
tleft.left(20)
tleft.penup()
tleft.forward(18)
tleft.pendown()
tleft.forward(50)#额头竖线
tleft.penup()
tleft.forward(110)#消除竖线
tleft.pendown()
tleft.left(90)
tleft.forward(30)
tleft.right(90)
tleft.forward(60)
tleft.right(90)
tleft.forward(60)
tleft.right(90)
tleft.forward(60)
tleft.right(90)
tleft.forward(40)
tleft.penup()
tleft.forward(30)
tleft.pendown()
tleft.left(90)
tleft.forward(30)
tleft.right(180)
tleft.forward(100)
tleft.right(90)
tleft.forward(80)
tleft.right(90)
tleft.forward(100)
tleft.penup()
tleft.goto(150,70)
tleft.pendown()
tleft.left(100)
tleft.forward(40)
tleft.right(80)
tleft.circle(-333,40)
tleft.right(160)
tleft.forward(230)
#右半部分
tleft.left(100)
tleft.forward(40)
tleft.left(80)
tleft.forward(20)
tleft.left(100)
tleft.forward(30)
tleft.right(100)
tleft.forward(20)
tleft.right(80)
tleft.forward(30)
tleft.left(80)
tleft.forward(20)
tleft.left(100)
tleft.forward(30)
tleft.right(100)
tleft.forward(20)
tleft.right(80)
tleft.forward(30)
tleft.left(80)
tleft.forward(20)
tleft.left(100)
tleft.forward(30)
tleft.right(100)
tleft.forward(20)
tleft.right(80)
tleft.forward(30)
tleft.left(80)
tleft.forward(20)
tleft.left(100)
tleft.forward(30)
tleft.right(100)
tleft.forward(20)
tleft.right(80)
tleft.forward(30)
tleft.left(80)
tleft.forward(20)
tleft.left(100)
tleft.forward(30)
tleft.right(100)
tleft.forward(20)
tleft.right(80)
tleft.forward(30)
tleft.left(80)
tleft.forward(20)
tleft.left(100)
tleft.forward(30)
tleft.right(100)
tleft.forward(20)
tleft.right(80)
tleft.forward(30)
#右下部分
tleft.left(70)
tleft.forward(30)
tleft.right(110)
tleft.forward(40)
tleft.right(60)
tleft.forward(100)
tleft.right(30)
tleft.circle(200,20)
tleft.left(10)
tleft.forward(80)
#右下部分goto
tleft.penup()
tleft.goto(145,-198)
tleft.pendown()
tleft.left(90)
tleft.forward(30)
tleft.right(30)
tleft.forward(40)
tleft.right(150)
tleft.forward(30)
tleft.backward(30)
tleft.left(90)
tleft.forward(100)
tleft.right(90)
tleft.forward(30)
tleft.backward(30)
tleft.left(90)
tleft.right(30)
tleft.circle(200,20)
tleft.left(10)
tleft.forward(50)
#第三部分脸
t2=turtle.Turtle()
t2.penup()
t2.goto(0,-80)
#尖角
t2.circle(150,extent=90)
t2.pendown()
t2.circle(150,extent=30)
t2.penup()
t2.circle(150,extent=18)
t2.pendown()
t2.circle(150,extent=27)
t2.penup()
t2.circle(150,extent=30)
t2.pendown()
t2.circle(150,extent=27)
t2.penup()
t2.circle(150,extent=18)
t2.pendown()
t2.circle(150,extent=30)
t2.right(100)
t2.forward(40)
#左脸夹
t2.left(80)
t2.circle(333,40)
t2.left(160)
t2.forward(230)
#左半部分
t2.right(100)
t2.forward(40)
t2.right(80)
t2.forward(20)
t2.right(100)
t2.forward(30)
t2.left(100)
t2.forward(20)
t2.left(80)
t2.forward(30)
t2.right(80)
t2.forward(20)
t2.right(100)
t2.forward(30)
t2.left(100)
t2.forward(20)
t2.left(80)
t2.forward(30)
t2.right(80)
t2.forward(20)
t2.right(100)
t2.forward(30)
t2.left(100)
t2.forward(20)
t2.left(80)
t2.forward(30)
t2.right(80)
t2.forward(20)
t2.right(100)
t2.forward(30)
t2.left(100)
t2.forward(20)
t2.left(80)
t2.forward(30)
t2.right(80)
t2.forward(20)
t2.right(100)
t2.forward(30)
t2.left(100)
t2.forward(20)
t2.left(80)
t2.forward(30)
t2.right(80)
t2.forward(20)
t2.right(100)
t2.forward(30)
t2.left(100)
t2.forward(20)
t2.left(80)
t2.forward(30)
t2.right(70)
t2.forward(30)
t2.left(110)
t2.forward(40)
t2.left(60)
t2.forward(100)
t2.left(30)
t2.circle(-200,20)
t2.right(10)
t2.forward(80)
t2.penup()
t2.goto(-145,-198)#左脸颊
t2.pendown()
t2.right(90)
t2.forward(30)
t2.left(30)
t2.forward(40)
t2.left(150)
t2.forward(30)
t2.right(180)
t2.forward(30)
t2.left(90)
t2.forward(100)
t2.left(90)
t2.forward(30)
t2.left(180)
t2.forward(30)
t2.left(120)
t2.circle(-200,20)
t2.right(10)
t2.forward(50)
#左眼
t2.right(135)
t2.forward(70)
t2.left(50)
t2.forward(40)
t2.left(20)
t2.forward(20)
t2.penup()
t2.goto(-100,28)
t2.pendown()
t2.right(70)
t2.forward(65)
t2.left(50)
t2.forward(40)
t2.left(40)
t2.forward(20)
#左眼带
t2.penup()
t2.goto(-105,-10)
t2.pendown()
t2.right(100)
t2.circle(120,extent=20)
t2.circle(60,extent=80)
t2.penup()
t2.goto(-105,-13)
t2.pendown()
t2.right(100)
t2.circle(120,extent=20)
t2.circle(60,extent=80)
t2.penup()
t2.goto(-70,-40)
t2.pendown()
t2.left(10)
t2.forward(30)
t2.penup()
t2.goto(-10,-40)
t2.pendown()
t2.left(35)
t2.forward(30)
t2.penup()
t2.goto(-80,30)
t2.pendown()
t2.right(130)
t2.forward(47)
t2.left(50)
t2.forward(35)
t2.penup()
t2.goto(-60,-45)
t2.pendown()
t2.right(98)
t2.forward(60)
t2.left(20)
t2.forward(80)
t2.left(70)
t2.forward(10)
t2.left(90)
t2.forward(50)
t2.right(60)
t2.forward(30)
t2.right(60)
t2.forward(30)
t2.right(60)
t2.forward(50)
t2.left(90)
t2.forward(10)
t2.left(75)
t2.forward(80)
t2.left(15)
t2.forward(60)
t2.penup()
t2.goto(-80,-140)
t2.pendown()
t2.right(150)
t2.circle(85,extent=45)
t2.left(15)
t2.forward(70)
t2.left(15)
t2.circle(55,extent=55)
t2.penup()
t2.goto(0,-175)
t2.pendown()
t2.left(18)
t2.forward(170)
#右眼
tleft.left(135)
tleft.forward(70)
tleft.right(50)
tleft.forward(40)
tleft.right(20)
tleft.forward(20)
tleft.penup()
tleft.goto(100,28)
tleft.pendown()
tleft.left(70)
tleft.forward(65)
tleft.right(50)
tleft.forward(40)
tleft.right(40)
tleft.forward(20)
#右眼带
tleft.penup()
tleft.goto(105,-10)
tleft.pendown()
tleft.left(100)
tleft.circle(-120,extent=20)
tleft.circle(-60,extent=80)
tleft.penup()
tleft.goto(105,-13)
tleft.pendown()
tleft.left(100)
tleft.circle(-120,extent=20)
tleft.circle(-60,extent=80)
#右眼睛
tleft.penup()
tleft.goto(70,-40)
tleft.pendown()
tleft.right(10)
tleft.forward(30)
tleft.penup()
tleft.goto(10,-40)
tleft.pendown()
tleft.right(35)
tleft.forward(30)
tleft.penup()
tleft.goto(80,30)
tleft.pendown()
tleft.left(130)
tleft.forward(47)
tleft.right(50)
tleft.forward(35)
#鼻子
tleft.penup()
tleft.goto(0,-70)
tleft.pendown()
tleft.left(30)
tleft.forward(20)
tleft.left(72)
tleft.forward(10)
tleft.left(108)
tleft.forward(20)
tleft.right(42)
tleft.forward(20)
tleft.left(108)
tleft.forward(10)
tleft.left(72)
tleft.forward(20)
tleft.penup()
tleft.goto(0,-90)
tleft.pendown()
tleft.left(42)
tleft.forward(20)
tleft.left(72)
tleft.forward(10)
tleft.left(108)
tleft.forward(20)
tleft.right(42)
tleft.forward(20)
tleft.left(108)
tleft.forward(10)
tleft.left(72)
tleft.forward(20)
tleft.penup()
tleft.goto(200,500)
turtle.done()
