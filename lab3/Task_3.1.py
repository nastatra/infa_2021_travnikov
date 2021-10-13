import turtle as trl
from random import *

trl.shape('turtle')
trl.color('red')

for i in range(100):

    trl.forward(50*random())
    trl.left(360*(random()-0.5))

trl.exitonclick()