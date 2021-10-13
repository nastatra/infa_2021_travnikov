import turtle as trl

trl.shape('turtle')

def star(radius,n):

    for i in range(n):
        trl.forward(radius)
        trl.left(180 * (n - 1) / n)

trl.left(90)
trl.penup()
trl.goto(-100, 0)
trl.pendown()
trl.color('red')

n = 5
star(200,n)

trl.left(90)
trl.penup()
trl.goto(200, 0)
trl.pendown()
trl.color('blue')

n = 11
star(200,n)

trl.exitonclick()