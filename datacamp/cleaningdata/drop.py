import pandas as pd

titanic = pd.read_csv('./data/titanic.csv')

print(titanic)

# Select the 'age' and 'cabin' columns: df
df = titanic[['Age','Cabin']]

# Print the shape of df
print(df.shape)

# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape) # Drop row that any of its fields is NaN

# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape) # Drop row only if all fields are NaN

# Call .dropna() with thresh=1000 and axis='columns' and print the output of .info() from titanic
print(titanic.dropna(thresh=1000, axis='columns').info()) # Drop column where at least 1000 rows are NaN