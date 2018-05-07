import pandas as pd

df = pd.read_csv('./data/austin_airport_departure_data_2015_july.csv', index_col='Flight Number')
df.columns = df.columns.str.strip()

# Build a Boolean mask to filter out all the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df[mask]

# Combine two columns of data to create a datetime series: times_tz_none
times_tz_none = pd.to_datetime(la['Date'] + ' ' + la['Wheels-off Time'])

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')

print(times_tz_none.iloc[0])
print(times_tz_central.iloc[0])
print(times_tz_pacific.iloc[0])
