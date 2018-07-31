import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import CategoricalColorMapper
from bokeh.plotting import ColumnDataSource

# Read in the CSV file: df
df = pd.read_csv('./data/auto-mpg.csv')

df['color'] = ['blue' if origin == 'US' else 'red' if origin == 'Asia' else 'yellow' for origin in df['origin']]

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(df)

# Make a CategoricalColorMapper object: color_mapper
color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'],
                                      palette=['red', 'green', 'blue'])

p = figure(x_axis_label='WEIGHT', y_axis_label='MPG')

# Add a circle glyph to the figure p
p.circle('weight', 'mpg', source=source,
            color=dict(field='origin', transform=color_mapper),
            legend='origin')

# Specify the name of the output file and show the result
output_file('colormap.html')
show(p)
