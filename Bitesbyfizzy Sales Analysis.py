import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load the sales data
sales_data = pd.read_excel(r"c:\Users\PMLS\Desktop\Code In this folder for better organized\Bitesbyfizzy Order Details.xlsx")

# Chart 1: Top Selling Products
sns.barplot(x=sales_data.groupby('Products')['Products Sold'].sum().sort_values(ascending=False).head(10).index, color='#FF69B4',            y=sales_data.groupby('Products')['Products Sold'].sum().sort_values(ascending=False).head(10).values)
plt.title('Top Selling Products', fontweight='bold')
plt.xlabel('Products', fontweight='bold')
plt.ylabel('Total Products Sold', fontweight='bold')
plt.show()

# Chart 2: Revenue by city
sns.barplot(x='City', y='Net Price', data=sales_data.groupby('City')['Net Price'].sum().reset_index().sort_values(by='Net Price', ascending=False), color='#FF69B4')
plt.title('Revenue by City', fontweight='bold')
plt.xlabel('City', fontweight='bold')
plt.ylabel('Total Revenue', fontweight='bold')
plt.show()

# Sales Trend Over Time
sales_data.groupby('Order Month')['Net Price'].sum().plot(kind='line', color='#FC0FC0')
plt.title('Sales Trend Over Time', fontweight='bold')
plt.xlabel('Order Month', fontweight='bold')
plt.ylabel('Total Revenue', fontweight='bold')  
plt.show()

# Bestselling Flavors Analysis
sns.countplot(x='Flavour', data=sales_data, color="#FF69C6")
plt.title('Bestselling Flavors', fontweight='bold')
plt.xlabel('Flavours', fontweight='bold')
plt.ylabel('Count', fontweight='bold')
plt.show()

plt.savefig('bestselling_flavors.png')

# Summary Statistics 

print(sales_data.describe())
print(sales_data.nunique())
