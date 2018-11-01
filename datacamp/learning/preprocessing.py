# Import pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('./data/gapminder_tidy.csv')

# Create a boxplot of life expectancy per region
df.boxplot('life', 'region', rot=60)

# Show the plot
plt.show()


# Create dummy variables: df_region
df_region = pd.get_dummies(df)

# Print the columns of df_region
print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = pd.get_dummies(df,drop_first=True)

df_region = df_region.dropna(axis=0)

# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score, train_test_split

# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5, normalize=True)

X = df_region.drop('life',axis=1)
y = df_region['life']

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge,X,y, cv=5)

# Print the cross-validated scores
print(ridge_cv)


# Convert '?' to NaN
df[df == '?'] = np.nan

# Print the number of NaNs
print(df.isnull().sum())

# Print shape of original DataFrame
print("Shape of Original DataFrame: {}".format(df.shape))

# Drop missing values and print shape of new DataFrame
df_dropna = df.dropna()

# Print shape of new DataFrame
print("Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(df_dropna.shape))


