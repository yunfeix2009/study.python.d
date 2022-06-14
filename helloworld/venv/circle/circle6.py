import turtle

n = 500
turtle.pencolor("blue")
for i in range(1, 1000, 1):

    if i < 500:
        n = n - 1
        turtle.speed(100)
        turtle.fd(n)
        turtle.right(140)
    else:
        n += 1
        turtle.speed(100)
        turtle.pencolor('red')
        turtle.fd(n)
        turtle.right(114)
turtle.done()

