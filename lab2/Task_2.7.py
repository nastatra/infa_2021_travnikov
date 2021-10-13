import turtle

turtle.shape('turtle')
turtle.color('pink')

y=100

for i in range(1, 10*y, 1):
    turtle.forward(0.4+0.008*i)
    turtle.left(360/y)

turtle.exitonclick()