import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool

data = pd.read_csv('./data/gapminder_tidy.csv', index_col='Year')

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'x': data['fertility'][1970],
    'y': data['life'][1970],
    'country': data['Country'][1970],
})

# Create the figure: p
p = figure(title='1970', x_axis_label='Fertility (children per woman)', y_axis_label='Life Expectancy (years)',
           plot_height=400, plot_width=700,
           tools=[HoverTool(tooltips='@country')])

# Add a circle glyph to the figure p
p.circle(x='x', y='y', source=source)

# Output the file and show the figure
output_file('gapminder.html')
show(p)
