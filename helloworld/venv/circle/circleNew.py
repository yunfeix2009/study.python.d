import turtle as turtle

turtle.screensize(800, 600, "white")

turtle.pencolor('red')

turtle.circle(100)

for i in range(1,12):#每隔30度绘制一个三角形

    turtle.circle(100,steps=3)

    turtle.circle(100,30)