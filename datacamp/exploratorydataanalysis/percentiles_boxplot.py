import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./data/iris.csv')
versicolor_petal_length = df['petal length (cm)'][df['species'] == 'versicolor']
setosa_petal_length = df['petal length (cm)'][df['species'] == 'setosa']
virginica_petal_length = df['petal length (cm)'][df['species'] == 'virginica']


# Specify array of percentiles: percentiles
percentiles = np.array([2.5,25,50,75,97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length,percentiles)

# Print the result
print(ptiles_vers)

# Create box plot with Seaborn's default settings
sns.boxplot(x='species',y='petal length (cm)',data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal lenght (cm)')


# Show the plot
plt.show()