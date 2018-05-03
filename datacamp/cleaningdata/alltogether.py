from re import sub

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


gapminder = pd.read_csv("./data/gapminder.csv", index_col=0)

print(gapminder.head())

print(gapminder.info())

print(gapminder.describe())

print(gapminder.shape)

print(gapminder.columns)


# Create the scatter plot
gapminder.plot(kind='scatter', x='1800', y ='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()


def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()[1:-1]
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0


# Check whether the first column is 'Life expectancy'
assert gapminder.columns[-1] == 'Life expectancy'

# Check whether the values in the row are valid
assert gapminder.iloc[:, :-2].apply(check_null_or_valid, axis=1).all().all()

gapminder = gapminder.drop_duplicates(subset='Life expectancy')

# Check that there is only one instance of each country (value_counts()[0] contains the most frequently occuring value
assert gapminder['Life expectancy'].value_counts()[0] == 1

# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(gapminder, id_vars='Life expectancy')

# Rename the columns
gapminder_melt.columns = ['country','year','life_expectancy']

# Print the head of gapminder_melt
print(gapminder_melt.head())


# Convert the year column to numeric
gapminder_melt.year = pd.to_numeric(gapminder_melt.year)

# Test if country is of type object
assert gapminder_melt.country.dtypes == np.object

# Test if year is of type int64
assert gapminder_melt.year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gapminder_melt.life_expectancy.dtypes == np.float64
