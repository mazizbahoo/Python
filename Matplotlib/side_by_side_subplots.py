import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 50, 11)
y = t ** 2

plt.subplot(1, 2, 1)
plt.plot(t, y, 'r')

plt.subplot(1, 2, 2)
plt.plot(y, t, 'g')

plt.show()