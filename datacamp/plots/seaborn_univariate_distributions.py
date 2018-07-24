# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

auto = pd.read_csv('./data/auto-mpg.csv')

# JOINT DISTRIBUTIONS (2 pairs of variables)

# Generate a joint plot of 'hp' and 'mpg'
sns.jointplot(x='hp', y='mpg', data=auto)

# Display the plot
plt.show()

# kind='scatter' uses a scatter plot of the data points
# kind='reg' uses a regression plot (default order 1)
# kind='resid' uses a residual plot
# kind='kde' uses a kernel density estimate of the joint distribution
# kind='hex' uses a hexbin plot of the joint distribution

# Generate a joint plot of 'hp' and 'mpg' using a hexbin plot
sns.jointplot(x='hp', y='mpg', data=auto, kind='hex')

# Display the plot
plt.show()

# PAIRWISE DISTRIBUTIONS (many variables comparable in pairs)

# Plot the pairwise joint distributions from the DataFrame
sns.pairplot(auto[['mpg', 'hp']])

# Display the plot
plt.show()

# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
sns.pairplot(auto[['mpg', 'hp', 'origin']], kind='reg', hue='origin')

# Display the plot
plt.show()


# HEATMAP

corr_matrix = auto[['mpg','hp','weight','accel','displ']].corr()
# Visualize the covariance matrix using a heatmap
sns.heatmap(corr_matrix,)

# Display the heatmap
plt.show()
