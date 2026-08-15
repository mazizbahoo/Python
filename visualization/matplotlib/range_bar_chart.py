import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

a = np.array(["50-59", "60-69", "70-79", "80-89", "90-100"])
b = np.array([5, 6, 8, 7, 4])

ax.bar(a, b, edgecolor='blue', linewidth=1)

ax.set_title('Percentage of Students in Different Ranges')
ax.set_xlabel('Percentage Ranges')
ax.set_ylabel('No. of Students')

plt.tight_layout()
plt.show()