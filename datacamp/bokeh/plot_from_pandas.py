# Import pandas as pd
import pandas as pd
# Import figure from bokeh.plotting
from bokeh.plotting import figure
from bokeh.io import output_file, show

# Read in the CSV file: df
df = pd.read_csv('./data/auto-mpg.csv')

df['color'] = ['blue' if origin == 'US' else 'red' if origin == 'Asia' else 'yellow' for origin in df['origin']]

# Create the figure: p
p = figure(x_axis_label='HP', y_axis_label='MPG')

# Plot mpg vs hp by color
p.circle(df['hp'], df['mpg'], color=df['color'], size=10)

# Specify the name of the output file and show the result
output_file('auto-df.html')
show(p)
