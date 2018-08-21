import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./data/iris.csv')

# Create bee swarm plot with Seaborn's default settings
sns.swarmplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')
# Show the plot
plt.show()
