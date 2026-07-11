import matplotlib.pyplot as plt
import numpy as np

v = 40
t = np.linspace(0, 50, 11)
d = v * t

plt.plot(t, d, 'g')
plt.title('Distance Time Graph')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.show()