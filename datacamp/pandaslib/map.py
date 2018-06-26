import pandas as pd

titanic = pd.read_csv('./data/titanic.csv')

# Create the Boolean Series: under10
under10 = (titanic['Age'] < 10).map({True:'under 10', False: 'over 10'})

# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['Survived'].mean()
print(survived_mean_1)

# Group by under10 and pclass and compute the survival rate
survived_mean_2 = titanic.groupby([under10, 'Pclass'])['Survived'].mean()
print(survived_mean_2)