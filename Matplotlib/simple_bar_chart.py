import matplotlib.pyplot as plt

data = {'C++': 20, 'Python': 15, 'Java': 30, 'C#': 10}
languages = list(data.keys())
students = list(data.values())

plt.bar(languages, students, color='maroon', width=0.4)
plt.title('Number of Students in Different Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Number of Students')
plt.show()