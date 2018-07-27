# Import figure from bokeh.plotting
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

aapl = pd.read_csv('./data/aapl.csv')
aapl['date'] = pd.to_datetime(aapl['date'])

# Create a figure with x_axis_type="datetime": p
p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')

# Plot date along the x axis and price along the y axis
p.line(aapl['date'], aapl['close'])

# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p.circle(aapl['date'], aapl['close'], fill_color='white', size=4)

# Specify the name of the output file and show the result
output_file('line.html')
show(p)
