import pandas as pd

# Initialize empty list: units
units = []

# Build the list of Series
jan = pd.read_csv('./data/sales-jan-2015.csv', index_col='Date', parse_dates=True)
feb = pd.read_csv('./data/sales-feb-2015.csv', index_col='Date', parse_dates=True)
mar = pd.read_csv('./data/sales-mar-2015.csv', index_col='Date', parse_dates=True)


for month in [jan, feb, mar]:
    units.append(month['Units'])

# Concatenate the list: quarter1
quarter1 = pd.concat(units, axis='rows')

# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])



# Concatenate weather_max and weather_mean horizontally: weather
#weather = pd.concat([weather_max, weather_mean], axis=1)

# Print weather
#print(weather)

medal_types = ['bronze','silver','gold']
medals = []
for medal in medal_types:
    # Create the file name: file_name
    file_name = "./data/%s_top5.csv" % medal

    # Create list of column names: columns
    columns = ['Country', medal]

    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=columns)

    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals, axis='columns')

# Print medals
print(medals)