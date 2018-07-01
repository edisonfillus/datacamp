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


jan = pd.read_csv('./data/sales-jan-2015.csv')
feb = pd.read_csv('./data/sales-feb-2015.csv')
mar = pd.read_csv('./data/sales-mar-2015.csv')

# Make the list of tuples: month_list
month_list = [('january',jan),('february',feb),('march',mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)

# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])



########## INNER JOIN ####################

bronze = pd.read_csv('./data/bronze_top5.csv', index_col='Country')
silver = pd.read_csv('./data/silver_top5.csv', index_col='Country')
gold = pd.read_csv('./data/gold_top5.csv', index_col='Country')

medal_list = [bronze, silver, gold]
# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list, keys=['bronze', 'silver', 'gold'], axis=1, join='inner')

# Print medals
print(medals)


###### RESAMPLE AND INNER JOIN ###########

us = pd.read_csv('./data/gdp_usa.csv', index_col='Year', parse_dates=True)
china = pd.read_csv('./data/gdp_china.csv', index_col='Year', parse_dates=True)

# Resample and tidy china: china_annual
china_annual = china.resample('A').mean().pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').mean().pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual,us_annual],axis=1, join='inner')

# Resample gdp and print
print(gdp.resample('10A').last())