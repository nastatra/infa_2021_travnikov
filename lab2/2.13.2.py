import turtle as trl
import numpy as np

trl.shape('turtle')

# Function plotting circle
def circle(radius,direction):
    n=200
    length = radius * 2 * np.sin(np.pi / n)
    for i in range(n):
        trl.forward(length)
        if direction == 'left':
            trl.left(360 / n)
        else:
            trl.right(360 / n)

# Function plotting arc
def arc(radius):
    n=200
    length = radius * 2 * np.sin(np.pi / n)
    for i in range(int(n/2)):
        trl.forward(length)
        trl.right(360 / n)

# Function plotting face
def plot_face(R, X, Y):
    trl.penup()
    trl.goto(X, Y-R)
    trl.pendown()
    trl.color('black')
    trl.begin_fill()
    circle(R, 'left')
    trl.color('yellow')
    trl.end_fill()

# Function plotting eye
def plot_eye(R, X, Y):
    trl.penup()
    trl.goto(X, Y-R)
    trl.pendown()
    trl.color('black')
    trl.begin_fill()
    circle(R, 'left')
    trl.color('blue')
    trl.end_fill()

# Function plotting nose
def plot_nose(L, X, Y):
    trl.penup()
    trl.goto(X, Y)
    trl.pendown()
    trl.left(270)
    trl.color('black')
    trl.width(8)
    trl.forward(L)

# Function ploting mouth
def plot_mouth(R, X, Y):
    trl.penup()
    trl.goto(X, Y)
    trl.pendown()
    trl.color('red')
    trl.width(8)
    arc(R)

# Plot face
plot_face(100, 0, 0)
# Plot left eye
plot_eye(10, -40, 40)
# Plot right eye
plot_eye(10, 40, 40)
# Plot nose
plot_nose(30, 0, 10)
# Plot mouth
plot_mouth(40, 40, -20)

trl.exitonclick()