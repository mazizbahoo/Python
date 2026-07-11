import matplotlib.pyplot as plt
import numpy as np

# v = 40
# t = np.linspace(0, 50, 11)
# d = v * t
# plt.plot(t, d, 'g')
# plt.title('Distance Time Graph')
# plt.xlabel('Time (s)')
# plt.ylabel('Distance (m)')
# plt.show()

# x = t = np.linspace(0, 50, 11)
# y = t ** 2
# plt.subplot(1, 2, 1)
# plt.plot(t, y, 'r')
# plt.subplot(1, 2, 2)
# plt.plot(y, t, 'g')
# plt.show()

# Graph Inside Graph
# plt.figure()
# x = np.linspace(0, 50, 11)
# y = x ** 2
# plt.plot(x, y, 'r')
# plt.title('Distance Time Graph')
# plt.xlabel('Time (s)')
# plt.ylabel('Distance (m)')
# plt.axes([0.25, 0.5, 0.3, 0.3])
# plt.plot(y, x, 'g')
# plt.title('Distance Time Graph')
# plt.xlabel('Distance (m)')
# plt.ylabel('Time (s)')
# plt.show()

# fig, axes = plt.subplots(2, 2, figsize=(10, 8)) # Added figsize to give it more breathing room
# x = np.linspace(0, 50, 11)
# y = x ** 2
# axes[0, 0].plot(x, y, 'r', linewidth=2)
# axes[0, 0].set_title('Time vs Distance')
# axes[0, 0].set_xlabel('Time (s)')
# axes[0, 0].set_ylabel('Distance (m)')

# axes[0, 1].plot(y, x, 'g', linewidth=2)
# axes[0, 1].set_title('Distance vs Time')
# axes[0, 1].set_xlabel('Distance (m)')
# axes[0, 1].set_ylabel('Time (s)')

# axes[1, 0].plot(x, y, 'b', linewidth=2)
# axes[1, 0].set_title('Time vs Distance (Alt)')
# axes[1, 0].set_xlabel('Time (s)')
# axes[1, 0].set_ylabel('Distance (m)')

# axes[1, 1].plot(y, x, 'y', linewidth=2)
# axes[1, 1].set_title('Distance vs Time (Alt)')
# axes[1, 1].set_xlabel('Distance (m)')
# axes[1, 1].set_ylabel('Time (s)')

# plt.tight_layout()
# plt.show()

# Bar Plots 
# data = {'C++': 20, 'Python': 15, 'Java': 30, 'C#': 10}
# languages = list(data.keys())
# students = list(data.values())
# plt.bar(languages, students, color='maroon', width=0.4)
# plt.title('Number of Students in Different Programming Languages')
# plt.xlabel('Programming Languages')
# plt.ylabel('Number of Students')
# plt.show()