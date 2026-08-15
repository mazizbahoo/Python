import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
flights = sns.load_dataset('flights')
penguins = sns.load_dataset('penguins')
titanic = sns.load_dataset('titanic')

sns.set_style("whitegrid")

sns.lineplot(x='year', y='passengers', data=flights, hue='month', errorbar=None)
plt.show()

sns.regplot(x='total_bill', y='tip', data=tips, order=2, ci=95, marker='+')
plt.show()

sns.lmplot(x='total_bill', y='tip', data=tips, hue='smoker', col='time', row='sex', markers=['o', 'x'])
plt.show()

sns.residplot(x='total_bill', y='tip', data=tips, lowess=True)
plt.show()

sns.kdeplot(data=tips, x='total_bill', hue='time', multiple='stack', fill=True, bw_adjust=0.5)
plt.show()

sns.ecdfplot(data=penguins, x='flipper_length_mm', hue='species', stat='proportion')
plt.show()

sns.scatterplot(data=tips, x='total_bill', y='tip')
sns.rugplot(data=tips, x='total_bill', y='tip', height=0.1)
plt.show()

sns.stripplot(x='day', y='total_bill', data=tips, hue='smoker', jitter=True, dodge=True)
plt.show()

sns.swarmplot(x='day', y='total_bill', data=tips, hue='sex', dodge=True, size=4, palette='Set2')
plt.show()

sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker', notch=True, width=0.5)
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True, inner='quartile')
plt.show()

sns.boxenplot(x='day', y='total_bill', data=tips, hue='time', width=0.8)
plt.show()

sns.pointplot(x='time', y='total_bill', data=tips, hue='smoker', markers=['o', 's'], linestyles=['-', '--'], dodge=True)
plt.show()

sns.countplot(x='deck', data=titanic, hue='class')
plt.show()

corr=titanic.select_dtypes(include='number').corr()
sns.heatmap(corr,annot=True, cmap='coolwarm')
plt.show()

sns.clustermap(flights_pivot, metric='correlation', method='single', standard_scale=1, figsize=(6, 6))
plt.show()

sns.pairplot(iris, hue='species', vars=['sepal_length', 'sepal_width'], kind='reg', diag_kind='kde')
plt.show()

sns.jointplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species', kind='kde', fill=True)
plt.show()

corr = tips.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

sns.distplot(titanic['fare'].dropna(), bins=30, color='blue')
plt.show()