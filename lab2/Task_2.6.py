import turtle as trl

n = 12

trl.shape('turtle')
trl.color('cyan')

for i in range(1, n+1, 1):
    trl.right(360/n)
    trl.forward(150)
    trl.stamp()
    trl.backward(150)
