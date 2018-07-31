# Import pandas as pd
import pandas as pd
# Import figure from bokeh.plotting
from bokeh.plotting import figure
from bokeh.io import output_file, show
# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Read in the CSV file: df
df = pd.read_csv('./data/auto-mpg.csv')
df['color'] = ['blue' if origin == 'US' else 'red' if origin == 'Asia' else 'yellow' for origin in df['origin']]

# Create a ColumnDataSource from df: source
source = ColumnDataSource(df)

p = figure(x_axis_label='MPG', y_axis_label='HP')

# Add circle glyphs to the figure p
p.circle('mpg', 'hp', size=8, source=source, color='color')

# Specify the name of the output file and show the result
output_file('sprint.html')
show(p)
