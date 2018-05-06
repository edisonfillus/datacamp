import pandas as pd

df = pd.read_csv('./data/weather_data_austin_2010.csv', parse_dates=True, index_col='Date')
print(df)

# Downsample to 6 hour data and aggregate by mean: df1
df1 = df['Temperature'].resample('6h').mean()

print(df1)

# Downsample to daily data and count the number of data points: df2
df2 = df['Temperature'].resample('D').count()

print(df2)

# Extract temperature data for August: august
august = df['Temperature']['2010-08']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

print(august_highs)

# Extract temperature data for February: february
february = df['Temperature']['2010-02']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()

print(february_lows)