import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 2*(np.pi), 0.00001)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

plt.figure(figsize=(9, 9))
plt.plot(x, y, 'r')

plt.xticks([])
plt.yticks([])
plt.box(False)
plt.show()