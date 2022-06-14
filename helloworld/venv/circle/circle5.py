import turtle

turtle.penup()
turtle.goto(-450, 300)
turtle.pendown()
turtle.speed(100)
n = 800
for i in range(10000):
    n -= 1
    if 800 >= n > 700:
        turtle.pencolor('purple')
    elif 700 >= n > 600:
        turtle.pencolor("indigo")
    elif 600 >= n > 500:
        turtle.pencolor("blue")
    elif 500 >= n > 400:
        turtle.pencolor("green")
    elif 400 >= n > 300:
        turtle.pencolor("yellow")
    elif 300 >= n > 200:
        turtle.pencolor("orange")
    elif 200 >= n > 100:
        turtle.pencolor("red")
    elif n > 0:
        turtle.pencolor("black")
    # else:
    #     turtle.pendone()
    elif n <= -800:
        turtle.pendone()
        # turtle.pencolor("white")
    else:
        turtle.pencolor("black")
    turtle.fd(n)
    turtle.right(90)
