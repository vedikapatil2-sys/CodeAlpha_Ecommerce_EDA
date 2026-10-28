# CodeAlpha Ecommerce EDA - Vedika Patil CA/DF1/327215
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Ecommerce_Sales_Sample.csv')
print(df.head())
print(df.describe())

# Visualization
sns.barplot(x='Category', y='Sales', data=df, estimator=sum)
plt.title('Sales by Category')
plt.show()
