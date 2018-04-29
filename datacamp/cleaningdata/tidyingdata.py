import pandas as pd
import numpy as np

airquality = pd.read_csv('./data/airquality.csv')

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = pd.pivot_table(airquality_melt, index=['Month', 'Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the new index of airquality_pivot
print(airquality_pivot.index)

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Duplicate some observations
airquality_dup = airquality_melt.append(airquality_melt[:0 - 30])

# Print the new shape
print(airquality_dup.shape)

# Pivot airquality_dup: airquality_pivot
airquality_pivot = pd.pivot_table(airquality_dup, index=['Month', 'Day'], columns='measurement', values='reading',
                                  aggfunc=np.mean)

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())
