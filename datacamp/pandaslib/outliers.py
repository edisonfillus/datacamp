# Import zscore
from scipy.stats import zscore
import pandas as pd

# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('./data/gapminder_tidy.csv', index_col=['Country']).sort_index()

gapminder_2010 = gapminder[gapminder['Year'] == 2010]

# Group gapminder_2010: standardized
standardized = gapminder_2010.groupby('region')[['life','fertility']].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = ((standardized['life'] < -3) | (standardized['fertility'] > 3))

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder_2010.loc[outliers]

# Print gm_outliers
print(gm_outliers)