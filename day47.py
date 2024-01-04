#Create a data visualization using a library like Matplotlib
print ("\nWilson - Day 47 of #100DaysOfCode\n") 
print("\nCreate a data visualization using a library like Matplotlib\n")

import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May']
sales = [50000, 60000, 75000, 90000, 80000]

plt.bar(months, sales, color='blue')

plt.title('Monthly Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales ($USD)')
plt.show()

#Create a data visualization using a library like Seaborn

import seaborn as sns
import pandas as pd

data = pd.DataFrame({'X': [1, 2, 3, 4, 5],'Y': [10, 8, 15, 7, 12]})

sns.scatterplot(x='X', y='Y', data=data)

plt.title('Scatter Plot with Seaborn')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
