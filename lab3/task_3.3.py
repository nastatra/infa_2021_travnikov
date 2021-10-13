import turtle as trl

trl.shape('circle')
trl.color('blue')

ay = -9.8

dt = 0.05
x = -300
y = 0.1
Vx = 10
Vy = 60

trl.penup()
trl.goto(300, 0)
trl.pendown()
trl.goto(x, y)

for i in range(10):

    while y >= 0:
        Vy += ay * dt
        x += Vx * dt
        y += Vy * dt + ay * dt ** 2 / 2

        trl.goto(x, y)

    y = 0
    Vy = -Vy * 0.85

trl.exitonclick()