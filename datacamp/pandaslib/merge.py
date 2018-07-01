import pandas as pd

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



# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')

print(m2m.head(20))

survey = pd.DataFrame(
    {
        'taken':[619,619,622,622,734,734,734,735, 735, 735, 751,751,751,752,752, 752, 837,837,837,844],
        'person':['dyer','dyer','dyer','dyer', 'pb', 'lake','pb','pb', 'NaN', 'NaN', 'pb','pb', 'lake','lake','lake','lake', 'roe','lake''lake','roe', 'roe'],
        'quant':['rad','sal','rad','sal','rad','sal','rad','sal','rad','sal','rad','sal','rad','sal','rad','sal','rad','sal','rad','sal'],
        'reading':[9.82, 0.13, 7.80, 0.09,9.82, 0.13, 7.80, 0.09,9.82, 0.13, 7.80, 0.09,9.82, 0.13, 7.80, 0.09,9.82, 0.13, 7.80, 0.09]
    }
)

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')

# Print the first 20 lines of m2m
print(m2m.head(20))


revenue = pd.DataFrame(columns=['branch_id','city','revenue','state'])
sales=pd.DataFrame(columns=['city','state','units'])
managers = pd.DataFrame(columns=['branch','branch_id','manager','state'])

# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue, sales, how='inner', on=['city','state'])

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales, managers, how='inner', left_on=['city','state'], right_on=['branch', 'state'])

# Merge all
merge_default = pd.merge(sales_and_managers, revenue_and_sales, how='inner', on=['city','state'])


