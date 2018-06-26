import pandas as pd

ebola = pd.read_csv('./data/ebola.csv')

# Fill the missing values with the mean
ebola = ebola.fillna(ebola.mean())

# Assert that there are no missing values
assert pd.notnull(ebola).all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()