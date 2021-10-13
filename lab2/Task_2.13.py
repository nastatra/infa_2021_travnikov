import turtle as trl
import numpy as np

trl.shape('turtle')

def circle(radius,direction):
    n=200
    length = radius * 2 * np.sin(np.pi / n)
    for i in range(n):
        trl.forward(length)
        if direction == 'left':
            trl.left(360 / n)
        else:
            trl.right(360 / n)

def arc(radius):
    n=200
    length = radius * 2 * np.sin(np.pi / n)
    for i in range(int(n/2)):
        trl.forward(length)
        trl.right(360 / n)

R = 100
trl.penup()
trl.goto(R, 0)
trl.pendown()
trl.left(90)
trl.color('black')
trl.begin_fill()
circle(R,'left')
trl.color('yellow')
trl.end_fill()

R2 = R*0.1
trl.penup()
trl.goto(-R*0.4, R*0.5)
trl.pendown()
trl.left(90)
trl.color('black')
trl.begin_fill()
circle(R2,'left')
trl.color('blue')
trl.end_fill()

trl.penup()
trl.goto(R*0.3, R*0.4)
trl.pendown()
trl.left(90)
trl.color('black')
trl.begin_fill()
circle(R2,'left')
trl.color('blue')
trl.end_fill()

trl.penup()
trl.goto(0, R*0.1)
trl.pendown()
trl.color('black')
trl.width(8)
trl.forward(R*0.3)

R3=R*0.4
trl.penup()
trl.goto(R3, -R*0.2)
trl.pendown()
trl.color('red')
trl.width(8)
arc(R3)

trl.exitonclick()