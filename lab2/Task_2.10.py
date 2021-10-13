import turtle as trl
import numpy as np

trl.shape('turtle')
trl.color('pink')

def circle(radius,direction):
    n=300
    length = radius * 2 * np.sin(np.pi / n)
    for i in range(n+1):
        trl.forward(length)
        if direction == 'left':
            trl.left(360 / n)
        else:
            trl.right(360 / n)

number = 8
for n in range(int(number/2)):

    circle(50,'left')
    circle(50,'right')

    trl.left(360/number)

trl.exitonclick()