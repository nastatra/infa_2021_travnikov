import turtle as trl
import numpy as np

trl.shape('turtle')
trl.color('green')

def arc(radius):
    n=100
    length = radius * 2 * np.sin(np.pi / n)
    for i in range(n):
        trl.forward(length)
        trl.right(180 / n)

trl.left(90)
trl.penup()
trl.goto(-200, 0)
trl.pendown()

number = 4
for n in range(number):

    arc(30)
    arc(5)

trl.exitonclick()