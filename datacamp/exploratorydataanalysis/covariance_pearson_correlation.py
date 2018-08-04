import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./data/iris.csv')
versicolor_petal_length = df['petal length (cm)'][df['species'] == 'versicolor']
versicolor_petal_width = df['petal width (cm)'][df['species'] == 'versicolor']

# Make a scatter plot
plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')

# Label the axes
plt.xlabel('Petal length')
plt.ylabel('Petal width')

# Show the result
plt.show()

# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0, 1]

# Print the length/width covariance
print('Covariance: ', petal_cov)

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x,y)

    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length,versicolor_petal_width)

# Print the result
print('Pearson Correlation: ', r)
