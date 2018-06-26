import pandas as pd

titanic = pd.read_csv('./data/titanic.csv')

# Create a groupby object: by_sex_class
by_sex_class = titanic.groupby(['Sex','Pclass'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())

# Impute age and assign to titanic['age']
titanic.age = by_sex_class['Age'].transform(impute_median) #Will use the median of Same Sex and Pclass

# Print the output of titanic.tail(10)
print(titanic.tail(10))