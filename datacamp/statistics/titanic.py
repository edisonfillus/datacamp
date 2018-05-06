import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('./data/titanic.csv')

print(titanic.head())

# Display the box plots on 3 separate rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1)

# Generate a box plot of the fare prices for the First passenger class
titanic.loc[titanic['Pclass'] == 1].plot(ax=axes[0], y='Fare', kind='box')

# Generate a box plot of the fare prices for the Second passenger class
titanic.loc[titanic['Pclass'] == 2].plot(ax=axes[1], y='Fare', kind='box')

# Generate a box plot of the fare prices for the Third passenger class
titanic.loc[titanic['Pclass'] == 3].plot(ax=axes[2], y='Fare', kind='box')

# Display the plot
plt.show()