import pandas as pd

# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('./data/gapminder_tidy.csv', index_col=['Country']).sort_index()

gapminder_2010 = gapminder[gapminder['Year'] == 2010]

# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')

def disparity(gr):
    # Compute the spread of gr['gdp']: s
    s = gr['gdp'].max() - gr['gdp'].min()
    # Compute the z-score of gr['gdp'] as (gr['gdp']-gr['gdp'].mean())/gr['gdp'].std(): z
    z = (gr['gdp'] - gr['gdp'].mean())/gr['gdp'].std()
    # Return a DataFrame with the inputs {'z(gdp)':z, 'regional spread(gdp)':s}
    return pd.DataFrame({'z(gdp)':z , 'regional spread(gdp)':s})


# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)  # for each group

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[['United States','United Kingdom','China']])
