import pandas as pd
import numpy as np

df = pd.read_csv('./data/iris.csv')
versicolor_petal_length = df['petal length (cm)'][df['species'] == 'versicolor']
setosa_petal_length = df['petal length (cm)'][df['species'] == 'setosa']
virginica_petal_length = df['petal length (cm)'][df['species'] == 'virginica']

# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = differences ** 2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results
print(variance_np, variance_explicit)

# Print the square root of the variance and standard deviation using NumPy
print(np.sqrt(variance_np), np.std(versicolor_petal_length))
