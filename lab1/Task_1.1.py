import numpy as np

x = [1, 10, 1000]

for i in range(3):
    z = np.exp(1/(np.sin(x[i]) + 1)) / (5/4 + 1/(x[i]**1*5))
    y = np.log(z) / np.log(1 + x[i]**2)

    print(y)