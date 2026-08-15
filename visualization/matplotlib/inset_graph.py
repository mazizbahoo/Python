import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x = np.linspace(0, 50, 11)
y = x ** 2

# Main plot
plt.plot(x, y, 'r')
plt.title('Distance Time Graph')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')

# Inset plot
plt.axes([0.25, 0.5, 0.3, 0.3])
plt.plot(y, x, 'g')
plt.title('Distance Time Graph')
plt.xlabel('Distance (m)')
plt.ylabel('Time (s)')

plt.show()