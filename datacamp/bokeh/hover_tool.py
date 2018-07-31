import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource
import numpy as np

# import the HoverTool
from bokeh.models import HoverTool

# Create a figure with the "box_select" tool: p
p = figure(x_axis_label='Time of Day', y_axis_label='Blood Glucose (mg/dl)')

x = np.linspace(0, 287, 195)
y = np.concatenate(
    [np.linspace(80, 100, 40),
     np.linspace(100, 90, 20),
     np.linspace(90, 110, 40),
     np.linspace(110, 95, 20),
     np.linspace(95, 140, 10),
     np.linspace(140, 120, 5),
     np.linspace(120, 100, 20),
     np.linspace(100, 85, 40)])

# Add circle glyphs to figure p
p.circle(x, y, size=10,
         fill_color='grey', alpha=0.1, line_color=None,
         hover_fill_color='firebrick', hover_alpha=0.5,
         hover_line_color='white')

# Create a HoverTool: hover
hover = HoverTool(tooltips=None, mode='vline')

# Add the hover tool to the figure p
p.add_tools(hover)

# Specify the name of the output file and show the result
output_file('hover_glyph.html')
show(p)
