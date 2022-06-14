import turtle

n = 0
turtle.pencolor("blue")

for i in range(500):
    n = n + 1
    turtle.speed(100)
    turtle.fd(n)
    turtle.right(90)

turtle.pendone()

