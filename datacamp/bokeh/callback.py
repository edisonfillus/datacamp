# Create ColumnDataSource: source
import numpy as np
from bokeh.io import curdoc

from bokeh.layouts import widgetbox, column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure

x, y = 0

source = ColumnDataSource(data={'x':x,'y':y})

plot = figure()

# Add a line to the plot
plot.line('x', 'y', source=source)

slider = Slider(title='slider1', start=0, end=10, step=0.1, value=2)

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value',callback)


# Create a column layout: layout
layout = column(widgetbox(slider),plot)


# Add the layout to the current document
curdoc().add_root(layout)