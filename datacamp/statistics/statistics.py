import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/percent-bachelors-degrees-women-usa.csv', index_col='Year')

print(df.head())

# Print the minimum value of the Engineering column
print(df['Engineering'].min())

# Print the maximum value of the Engineering column
print(df['Engineering'].max())

# Construct the mean percentage per year: mean
mean = df.mean(axis='columns')

# Plot the average percentage per year
mean.plot()

# Display the plot
plt.show()


df = pd.read_csv('./data/titanic.csv')


# Print summary statistics of the fare column with .describe()
print(df['Fare'].describe())

# Generate a box plot of the fare column
df['Fare'].plot(kind='box')

# Show the plot
plt.show()