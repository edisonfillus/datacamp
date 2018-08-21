import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./data/iris.csv')
versicolor_petal_length = df['petal length (cm)'][df['species'] == 'versicolor']
setosa_petal_length = df['petal length (cm)'][df['species'] == 'setosa']
virginica_petal_length = df['petal length (cm)'][df['species'] == 'virginica']

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y


# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)

# Plot all ECDFs on the same plot
plt.plot(x_set,y_set, marker='.', linestyle='none')
plt.plot(x_vers,y_vers, marker='.', linestyle='none')
plt.plot(x_virg,y_virg, marker='.', linestyle='none')

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
plt.xlabel('petal length (cm)')
plt.ylabel('ECDF')

# Display the plot
plt.show()
