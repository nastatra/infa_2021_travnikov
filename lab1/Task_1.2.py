import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2.5, 3.51, 0.01)
plt.plot(x, x*x - x - 6)
plt.grid(True)
plt.show()