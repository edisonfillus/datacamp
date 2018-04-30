import pandas as pd
import glob

uber1 = pd.read_csv('./data/uber1.csv')
uber2 = pd.read_csv('./data/uber2.csv')
uber3 = pd.read_csv('./data/uber3.csv')


# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1,uber2,uber3])

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())


ebola = pd.read_csv('./data/ebola.csv')

# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=["Date", "Day"], var_name='type_country', value_name='counts')

status_country = pd.DataFrame()

status_country['status'] = ebola_melt['type_country'].str.split('_').str.get(0)
status_country['country'] = ebola_melt['type_country'].str.split('_').str.get(1)

del ebola_melt['type_country']

# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())


uber_csv_files = glob.glob('./data/uber?.csv')

print(uber_csv_files)

# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in uber_csv_files:
    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)

    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)
uber = uber.sort_values(by=['Date/Time'])

# Print the shape of uber
# Print the shape of uber
print(uber.shape)

# Print the head of uber
print(uber.head())


site = pd.DataFrame({'name': ['DR-1', 'DR-3' ,'MSK-4'], 'lat': [-49.85, -47.15, -48.87], 'long':[-128.57, -126.72,  -123.40]})
visited = pd.DataFrame({'site': ['DR-1', 'DR-3' ,'MSK-4'], 'ident': [619, 734, 837], 'dated':['1927-02-08', '1939-01-07','1932-01-14']})

# Merge the DataFrames: o2o - One to One
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(o2o)

visited = pd.DataFrame(
    {'site': ['DR-1', 'DR-3' , 'DR-3', 'DR-3', 'DR-3','MSK-4', 'DR-1'],
     'ident':[622, 734, 735, 751, 752, 837, 844],
     'dated':['1927-02-08', '1939-01-07','1930-01-12', '1930-02-26', 'NaN', '1932-01-14', '1932-03-22']
     })

# Merge the DataFrames: m2o - Many to One
m2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print m2o
print(m2o)

survey = pd.DataFrame(
    {
        'taken':[619,619,622,622,734,734,734,735, 735, 735, 751,751,751,752,752, 752, 837,837,837,844],
        'person':['dyer','dyer','dyer','dyer', 'pb', 'lake','pb','pb', 'NaN', 'NaN', 'pb','pb', 'lake','lake','lake','lake', 'roe','lake''lake','roe', 'roe'],
        'quant':['rad','sal','rad','sal','rad','sal','rad','sal','rad','sal','rad','sal','rad','sal','rad','sal','rad','sal','rad','sal'],
        'reading':[9.82, 0.13, 7.80, 0.09,9.82, 0.13, 7.80, 0.09,9.82, 0.13, 7.80, 0.09,9.82, 0.13, 7.80, 0.09,9.82, 0.13, 7.80, 0.09]
    }
)

# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')

# Print the first 20 lines of m2m
print(m2m.head(20))
