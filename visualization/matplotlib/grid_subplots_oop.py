import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
x = np.linspace(0, 50, 11)
y = x ** 2

# Top-Left
axes[0, 0].plot(x, y, 'r', linewidth=2)
axes[0, 0].set_title('Time vs Distance')
axes[0, 0].set_xlabel('Time (s)')
axes[0, 0].set_ylabel('Distance (m)')

# Top-Right
axes[0, 1].plot(y, x, 'g', linewidth=2)
axes[0, 1].set_title('Distance vs Time')
axes[0, 1].set_xlabel('Distance (m)')
axes[0, 1].set_ylabel('Time (s)')

# Bottom-Left
axes[1, 0].plot(x, y, 'b', linewidth=2)
axes[1, 0].set_title('Time vs Distance (Alt)')
axes[1, 0].set_xlabel('Time (s)')
axes[1, 0].set_ylabel('Distance (m)')

# Bottom-Right
axes[1, 1].plot(y, x, 'y', linewidth=2)
axes[1, 1].set_title('Distance vs Time (Alt)')
axes[1, 1].set_xlabel('Distance (m)')
axes[1, 1].set_ylabel('Time (s)')

plt.tight_layout()
plt.show()