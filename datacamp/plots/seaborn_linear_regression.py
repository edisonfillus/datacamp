# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

auto = pd.read_csv('./data/auto-mpg.csv')

# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x='weight', y='hp', data=auto)

# Display the plot
plt.show()

# RESIDUAL PLOT
# Visualizing how far datapoints diverge from the regression line

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')

# Display the plot
plt.show()

# 2nd ORDER REGRESSION

# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, color='blue', scatter=None, label='order 1')

# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, color='green', scatter=None, label='order 2', order=2)

# Add a legend and display the plot
plt.legend(loc='upper right')
plt.show()

# GROUPING LINEAR REGRESSIONS BY HUE

# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(x='weight', y='hp', data=auto, hue='origin', palette='Set1')

# Display the plot
plt.show()

# GROUPING LINEAR REGRESSIONS BY ROW OR COLUMN

# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight', y='hp', data=auto, row='origin')

# Display the plot
plt.show()
