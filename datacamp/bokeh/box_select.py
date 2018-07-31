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

# Create a figure with the "box_select" tool: p
p = figure(x_axis_label='MPG', y_axis_label='HP', tools='box_select')

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle('mpg', 'hp', selection_color='red', nonselection_alpha=0.1, source=source)

# Specify the name of the output file and show the result
output_file('selection_glyph.html')
show(p)
