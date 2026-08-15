import matplotlib.pyplot as plt

girls_grades = [49, 60, 35, 77, 65, 30, 75, 53, 46, 83]
boys_grades = [76, 48, 50, 83, 75, 89, 87, 67, 53, 97]
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fig, ax = plt.subplots(1, 1)

ax.scatter(hours_studied, boys_grades, color='b', label='Boys Grade')
ax.scatter(hours_studied, girls_grades, color='g', label='Girls Grade')

ax.set_xlabel('Hours Studied')
ax.set_ylabel('Grades Scored')
ax.set_title('Grades of Boys and Girls')
ax.legend()

plt.tight_layout()
plt.show()