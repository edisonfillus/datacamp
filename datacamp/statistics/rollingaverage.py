import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/weather_data_austin_2010.csv', parse_dates=True, index_col='Date')
print(df)

# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-Aug-01':'2010-Aug-15']

# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()

# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed': smoothed, 'unsmoothed': unsmoothed})

print(august)

# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()

# Extract the August 2010 data: august
august = df['Temperature']['2010-08']

# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = daily_highs.rolling(window=7).mean()
print(daily_highs_smoothed)

august = pd.DataFrame({'smoothed': daily_highs_smoothed, 'unsmoothed': daily_highs})

august.plot()
plt.show()
