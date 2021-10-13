import turtle as trl
import numpy as np

trl.shape('turtle')
trl.color('purple')

def polygon(n, length):
    for i in range(n):
        trl.forward(length)
        trl.left(360/n)

for n in range(3, 13):

    d=20
    R=d*(n-2)
    a=R*2*np.sin(np.pi/n)

    trl.penup()
    trl.forward(d)
    trl.pendown()
    trl.left(180*(n+2)/2/n)

    polygon(n, a)

    trl.right(180*(n+2)/2/n)

trl.exitonclick()