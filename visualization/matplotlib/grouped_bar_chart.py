import matplotlib.pyplot as plt
import numpy as np

data = [[20, 15, 30, 10], [35, 20, 25, 15], [32, 25, 15, 40]]
labels = ['2023', '2024', '2025', '2026']

x = np.arange(len(labels))
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ax.bar(x - 0.2, data[0], width=0.2, color='g', label='Computer Science')
ax.bar(x, data[1], width=0.2, color='r', label='Electrical Engineering')
ax.bar(x + 0.2, data[2], width=0.2, color='b', label='Mechanical Engineering')

ax.set_title('Number of Students in Bachelor Courses')
ax.set_xlabel('Years')
ax.set_ylabel('Number of Students')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.show()