from turtle import *
pensize(5)
speed(500)
bgcolor("black")
sides=eval(input("输入要绘制的边的数目，请输入2-6的数字！"))
colors=["red","yellow","green","blue","orange","purple"]
for x in range(500):
    pencolor(colors[x%sides])
    forward(x*3/sides+x)
    left(360/sides+1)
    width(x*sides/200)
done()
