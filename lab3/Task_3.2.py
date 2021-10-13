import turtle as trl
import numpy as np
from random import *

trl.shape('turtle')
trl.color('red')

a = 40

f0 = [(0,-a), (90, 2*a), (0, a), (-90, 2*a), (-180, a)]
f1 = [(0, 0), (45, a*np.sqrt(2)), (-90, 2*a)]
f2 = [(0, a), (0, a), (-90, a), (-135, a*np.sqrt(2)), (0, a)]
f3 = [(0, a), (0, a), (-135, a*np.sqrt(2)), (0, a), (-135, a*np.sqrt(2))]
f4 = [(0, a), (-90, a), (0, a), (90, a), (-90, 2*a)]
f5 = [(a, a), (-180, a), (-90, a), (0, a), (-90, a), (-180, a)]
f6 = [(a, a), (-135, a*np.sqrt(2)), (-90, a), (0, a), (90, a), (-180, a)]
f7 = [(0, a), (0, a), (-135, a*np.sqrt(2)), (-90, a)]
f8 = [(0,-a), (90, 2*a), (0, a), (-90, a), (-180, a), (0, a), (-90, a), (-180, a)]
f9 = [(a, 0), (-180, a), (90, a), (0, a), (-90, a), (-135, a*np.sqrt(2))]

number = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9]

start = -250
for n in 1, 4, 1, 7, 0, 0:

    start = start + int(1.5*a)
    trl.penup()
    trl.goto(start+int(number[n][0][0]),int(number[n][0][1]))
    trl.pendown()

    for i in range(1, len(number[n])):
        trl.setheading(int(number[n][i][0]))
        trl.forward(int(number[n][i][1]))

trl.exitonclick()
