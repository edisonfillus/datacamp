# Import package
import numpy as np
import matplotlib.pyplot as plt

# Assign filename to variable: file
file = '../../data/digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()



# Import numpy
import numpy as np

# Assign the filename: file
file = '../../data/digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

# Print data
print(data)



# Assign filename: file
file = '../../data/seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[10])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()


# Assign the filename: file
file = '../../data/titanic.csv'

# Import file using np.genfromtxt
data = np.genfromtxt(file, delimiter=',', names=True, dtype=None)
print(data['Survived'])

# Import file using np.recfromcsv. Defaults delimiter=',' and names=True in addition to dtype=None
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])