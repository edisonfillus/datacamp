import pandas as pd

# Read the raw file as-is: df1
df1 = pd.read_csv('./data/messy_stock_data.csv')

# Print the output of df1.head()
print(df1.head())

# Read in the file with the correct parameters: df2
df2 = pd.read_csv('./data/messy_stock_data.csv', delimiter=' ', header=3, comment='#')

# Print the output of df2.head()
print(df2.head())