from turtle import *
import time
import random
# speed(100)
#
# screensize(1500,1000)
# pensize(3)
# deg = random.randint(0,360)
# for i in range(250):
#     pencolor(0.34,0.245,0.21)
#     pencolor(int(random.randint(0,255))*0.001,int(random.randint(0,255))*0.001,int(random.randint(0,255))*0.001)
#     forward(5*i)
#     right(deg)
# time.sleep(200)
speed(100)
for i in range(12):
    for j in range(30):
        forward(5)
        right(3)
    penup()
    goto(0,0)
    pendown()