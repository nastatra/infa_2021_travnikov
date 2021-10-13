import turtle as trl

trl.shape('turtle')

d = 10
for i in range(1, 11, 1):
    trl.penup()
    trl.goto(-i*d, -i*d)
    trl.pendown()

    trl.forward(2*i*d)
    trl.left(90)
    trl.forward(2*i*d)
    trl.left(90)
    trl.forward(2*i*d)
    trl.left(90)
    trl.forward(2*i*d)
    trl.left(90)