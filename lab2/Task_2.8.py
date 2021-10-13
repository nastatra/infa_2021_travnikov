import turtle as trl

trl.shape('turtle')
trl.color('purple')

d = 10

s = d
for i in range(1, 11, 1):
    s = s + d
    trl.forward(s)
    trl.left(90)
    s = s + d
    trl.forward(s)
    trl.left(90)
    s = s + d
    trl.forward(s)
    trl.left(90)
    s = s + d
    trl.forward(s)
    trl.left(90)

trl.exitonclick()