import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

years = ['2023', '2024', '2025', '2026']
a_sales = [20000, 35000, 30000, 35000]
b_sales = [15000, 25000, 40000, 20000]

ax.bar(years, a_sales, label='Product A')
ax.bar(years, b_sales, bottom=a_sales, label='Product B')

ax.set_title('Sales of two products in a year.')
ax.set_xlabel('Years')
ax.set_ylabel('Sales')
ax.legend()

plt.tight_layout()
plt.show()