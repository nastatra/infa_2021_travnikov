import turtle as trl
import numpy as np

trl.shape('turtle')
trl.color('blue')

def circle(radius,direction):
    n=200
    length = radius * 2 * np.sin(np.pi / n)
    for i in range(n):
        trl.forward(length)
        if direction == 'left':
            trl.left(360 / n)
        else:
            trl.right(360 / n)

trl.left(90)

number = 8
for n in range(number):

    circle(20+10*(n+1),'left')
    circle(20+10*(n+1),'right')

trl.exitonclick()