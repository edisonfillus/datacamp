import pandas as pd
import matplotlib.pyplot as plt

# Read in the file with the correct parameters: df2
df = pd.read_csv('./data/messy_stock_data.csv', delimiter=' ', header=3, comment='#')


# Print the output of df2.head()
print(df.head())

df = pd.pivot_table(df, columns='name')


df.index = pd.to_datetime(df.index, format='%b')

df.index.name = 'Month'

print(df.index)


print(df.head())

# Create a list of y-axis column names: y_columns
y_columns = ['APPLE','IBM']

# Generate a line plot
df.plot(x=df.index, y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()
