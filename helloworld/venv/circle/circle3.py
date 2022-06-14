import turtle

n = 500
turtle.speed(100)
turtle.pencolor("blue")

for i in range(1000):

    if i < 700:
        n = n - 1
        turtle.fd(n)
        turtle.right(90)
    else:
        n += 1
        turtle.pencolor('red')
        turtle.fd(n)
        turtle.right(90)

turtle.pendone()

