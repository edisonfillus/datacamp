import pandas as pd

date_list = ['2010-10-01 10:00', '2010-10-01 11:00', '2010-10-02 10:00']
temperature_list = [12.3, 14.5, 13.4]

# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list, format=time_format)

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)

print(time_series)

print(time_series['2010-10-01'])
print(time_series['2010-10-01 21:00':'2010-10-02 10:00'])
