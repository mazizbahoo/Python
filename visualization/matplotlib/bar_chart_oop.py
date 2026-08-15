import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

data = {'C++': 20, 'Python': 15, 'Java': 30, 'C#': 10}
languages = list(data.keys())
students = list(data.values())

ax.bar(languages, students, color='maroon', width=0.4)
ax.set_title('Number of Students in Different Programming Languages')
ax.set_xlabel('Programming Languages')
ax.set_ylabel('Number of Students')

plt.show()