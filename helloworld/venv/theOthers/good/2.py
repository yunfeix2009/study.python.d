import turtle
t = turtle.Pen()
t.speed(500)
turtle.bgcolor("black")
sides=eval(input("输入要绘制的边的数目，请输入2-6的数字！"))
colors=["red","yellow","green","blue","orange","purple"]
for x in range(500):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)

print("####结束####")
