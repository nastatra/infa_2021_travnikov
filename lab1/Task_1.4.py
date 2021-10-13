import matplotlib.pyplot as plt

print('Input x1, y1:')
x1 = input()
y1 = input()

print('Input x2, y2:')
x2 = input()
y2 = input()

print('Input x3, y3:')
x3 = input()
y3 = input()

print('Input x4, y4:')
x4 = input()
y4 = input()

with plt.xkcd():
    plt.plot([x1, x2, x3, x4], [y1, y2, y3, y4])
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$y$', fontsize=14)

plt.show()