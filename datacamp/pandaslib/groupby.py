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



# Read life_fname into a DataFrame: life
life = pd.read_csv('./data/life_expectancy.csv', index_col='Country')

# Read regions_fname into a DataFrame: regions
regions = pd.read_csv('./data/regions.csv', index_col='Country')

# Group life by regions['region']: life_by_region
life_by_region = life.groupby(regions['region'])

# Print the mean over the '2010' column of life_by_region
print(life_by_region['2010'].mean())


titanic = pd.read_csv('./data/titanic.csv')

# Group titanic by 'pclass': by_class
by_class = titanic.groupby('Pclass')

# Select 'age' and 'fare'
by_class_sub = by_class[['Age','Fare']]

# Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max','median'])

# Print the maximum age in each class
print(aggregated.loc[:, ('Age','max')])

# Print the median fare in each class
print(aggregated.loc[:,('Fare','median')])



# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('./data/gapminder_tidy.csv', index_col=['Year','region','Country']).sort_index()

# Group gapminder by 'Year' and 'region': by_year_region
by_year_region = gapminder.groupby(level=['Year','region'])

# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()

# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Print the last 6 entries of aggregated
print(aggregated.tail(6))


# Read file: sales
sales = pd.read_csv('./data/sales.csv', index_col='Date', parse_dates=True)


# Create a groupby object: by_day
by_day = sales.groupby(sales.index.strftime('%a'))

# Create sum: units_sum
units_sum = by_day['Units'].sum()

# Print units_sum
print(units_sum)



# Group sales by 'Company': by_company
by_company = sales.groupby('Company')

# Compute the sum of the 'Units' of by_company: by_com_sum
by_com_sum = by_company['Units'].sum()
print(by_com_sum)

# Filter 'Units' where the sum is > 35: by_com_filt
by_com_filt = by_company.filter(lambda g:g['Units'].sum()>35)
print(by_com_filt)