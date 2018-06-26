import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv('./data/weather_data_austin_2010.csv', index_col='Date', parse_dates=True)
df = df[dt.datetime(2010, 1, 1): dt.datetime(2010, 1, 30)]

# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['DewPoint']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature', 'DewPoint']
df[column_list2].plot()
plt.show()
