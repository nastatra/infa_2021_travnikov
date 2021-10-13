import turtle

turtle.shape('turtle')
turtle.color('pink')
turtle.width(6)

y=300
turtle.begin_fill()
for i in range(1, y+1, 1):
    turtle.forward(2)
    turtle.left(360/y)
turtle.end_fill()

turtle.exitonclick()