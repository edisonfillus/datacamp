import pandas as pd

titanic = pd.read_csv('./data/titanic.csv')

# Group titanic by 'pclass'
by_class = titanic.groupby('Pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['Survived'].count()

# Print count_by_class
print(count_by_class)

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(['Embarked','Pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['Survived'].count()

# Print count_mult
print(count_mult)