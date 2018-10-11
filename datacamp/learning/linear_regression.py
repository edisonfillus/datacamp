# Import numpy and pandas
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Import LinearRegression
from sklearn.linear_model import LinearRegression

# Read the CSV file into a DataFrame: df
df = pd.read_csv('./data/gapminder_tidy.csv')

df = df.dropna()

sns.heatmap(df.corr(), square=True, cmap='RdYlGn')
plt.show()

# Create arrays for features and target variable
y = df['life']
X = df['fertility']

# Print the dimensions of X and y before reshaping
print("Dimensions of y before reshaping: {}".format(y.shape))
print("Dimensions of X before reshaping: {}".format(X.shape))

# Reshape X and y
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)

# Print the dimensions of X and y after reshaping
print("Dimensions of y after reshaping: {}".format(y.shape))
print("Dimensions of X after reshaping: {}".format(X.shape))

# Create the regressor: reg
reg = LinearRegression()

# Fit the model to the data
reg.fit(X, y)

# Create the prediction space
prediction_space = np.linspace(min(X), max(X)).reshape(-1, 1)

# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)

# Print R^2
print(reg.score(X,y))

# Plot regression line
plt.plot(X, y, color='blue', marker='.', linestyle='none')
plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.show()
