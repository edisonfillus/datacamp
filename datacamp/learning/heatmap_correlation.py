# Import numpy and pandas
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame: df
df = pd.read_csv('./data/gapminder_tidy.csv')

sns.heatmap(df.corr(), square=True, cmap='RdYlGn')
plt.show()