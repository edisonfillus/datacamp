import matplotlib.pyplot as plt
import numpy as np

female_literacy = np.array(
    [90.5, 50.8, 99.0, 88.8, 90.2, 40.0, 49.8, 48.8, 99.4, 99.0, 91.5, 93.9, 90.2, 99.0, 57.8, 22.8, 81.3,
     77.2, 91.5, 56.1, 99.0, 99.0, 98.5, 89.2, 88.1, 96.6, 99.6, 96.9, 93.4, 66.3, 59.6, 97.7, 82.8, 99.3,
     63.9, 99.0, 66.8, 44.1, 69.2, 12.6, 84.6, 45.4, 94.9, 98.9, 89.8, 80.2, 100.0, 59.3, 42.8, 40.1,
     96.9, 44.3, 77.2, 89.1, 65.3, 67.8, 57.0, 98.7, 99.0, 99.5, 21.6, 65.8, 15.1, 70.9, 68.7, 81.7, 18.2,
     61.0, 88.8, 33.0, 95.9, 99.8, 21.9, 99.0, 92.9, 99.0, 71.0, 98.9, 88.3, 26.4, 66.1, 86.0, 99.7, 99.0,
     99.2, 28.1, 59.9, 99.0, 97.9, 96.2, 83.5, 95.9, 99.5, 55.6, 53.7, 81.3, 93.5, 63.2, 81.4, 88.9, 77.9,
     28.9, 99.0, 100.0, 99.1, 99.3, 54.5, 91.6, 100.0, 96.2, 91.5, 98.0, 99.0, 41.1, 99.7, 99.0, 86.0,
     53.0, 95.9, 97.8, 92.8, 99.7, 98.5, 49.5, 98.7, 99.4, 80.9, 93.1, 90.8, 97.8, 99.8, 87.7, 95.1, 95.4,
     99.7, 83.5, 34.3, 36.5, 83.2, 99.8, 98.2, 90.4, 84.8, 85.6, 96.7, 89.4, 38.7, 89.1, 67.8, 90.7, 88.4,
     79.3, 93.5, 93.3, 96.5, 99.0, 98.4, 79.5, 98.5, 83.3, 98.0, 99.1])

illiteracy = 100 - female_literacy

fertility = np.array(
    [1.7690000000000001, 2.682, 2.077, 2.1319999999999997, 1.827, 3.872, 2.2880000000000003, 5.172999999999999,
     1.393, 1.262, 2.156, 3.0260000000000002, 2.033, 1.324, 2.8160000000000003, 5.211, 2.1, 1.781,
     1.8219999999999998, 5.9079999999999995, 1.881, 1.8519999999999999, 1.39, 2.281, 2.505, 1.224, 1.361,
     1.4680000000000002, 2.404, 5.52, 4.058, 2.2230000000000003, 4.859, 1.2670000000000001, 2.342, 1.579, 6.254,
     2.334, 3.9610000000000003, 6.505, 2.53, 2.823, 2.498, 2.248, 2.508, 3.04, 1.854, 4.22, 5.1, 4.967, 1.325,
     4.513999999999999, 3.173, 2.3080000000000003, 4.62, 4.541, 5.6370000000000005, 1.926, 1.7469999999999999,
     2.294, 5.841, 5.455, 7.069, 2.859, 4.018, 2.513, 5.405, 5.737, 3.363, 4.89, 1.385, 1.505, 6.081, 1.784,
     1.3780000000000001, 1.45, 1.841, 1.37, 2.612, 5.329, 5.33, 3.3710000000000004, 1.281, 1.871, 2.153,
     5.377999999999999, 4.45, 1.46, 1.436, 1.6119999999999999, 3.19, 2.752, 3.35, 4.01, 4.166, 2.642, 2.977,
     3.415, 2.295, 3.0189999999999997, 2.6830000000000003, 5.165, 1.849, 1.8359999999999999, 2.5180000000000002,
     2.43, 4.5280000000000005, 1.263, 1.885, 1.943, 1.899, 1.442, 1.953, 4.697, 1.5819999999999999, 2.025,
     1.841, 5.011, 1.212, 1.5019999999999998, 2.516, 1.367, 2.089, 4.388, 1.854, 1.7480000000000002, 2.978,
     2.1519999999999997, 2.362, 1.9880000000000002, 1.426, 3.29, 3.264, 1.436, 1.393, 2.822, 4.968999999999999,
     5.659, 3.24, 1.693, 1.6469999999999998, 2.36, 1.7919999999999998, 3.45, 1.516, 2.233, 2.563,
     5.2829999999999995, 3.885, 0.966, 2.373, 2.6630000000000003, 1.251, 2.052, 3.3710000000000004, 2.093, 2.0,
     3.883, 3.852, 3.718, 1.732, 3.928])


def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0, 1]


# Plot the illiteracy rate versus fertility
_ = plt.plot(fertility, illiteracy, marker='.', linestyle='none')

# Set the margins and label axes
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Show the plot
plt.show()

# Show the Pearson correlation coefficient
print(pearson_r(illiteracy, fertility))

# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(illiteracy, fertility, 1)

# Print the results to the screen
print('slope =', a, 'children per woman / percent illiterate')
print('intercept =', b, 'children per woman')

# Make theoretical line to plot
x = np.array([0, 100])
y = a * x + b

# Add regression line to your plot
_ = plt.plot(x, y)

# Draw the plot
plt.show()

# Specify slopes to consider: a_vals
a_vals = np.linspace(0, 0.1, 200)

# Initialize sum of square of residuals: rss
rss = np.empty_like(a_vals)

# Compute sum of square of residuals for each value of a_vals
for i, a in enumerate(a_vals):
    rss[i] = np.sum((fertility - a * illiteracy - b) ** 2)

# Plot the RSS
plt.plot(a_vals, rss, '-')
plt.xlabel('slope (children per woman / percent illiterate)')
plt.ylabel('sum of square of residuals')

plt.show()

# Anscombe
x = np.array([10., 8., 13., 9., 11., 14., 6., 4., 12., 7., 5.])
y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26,
              10.84, 4.82, 5.68])

# Perform linear regression: a, b
a, b = np.polyfit(x,y,1)

# Print the slope and intercept
print('slope =', a, ', intercept =',b)

# Generate theoretical x and y data: x_theor, y_theor
x_theor = np.array([3, 15])
y_theor = x_theor * a + b

# Plot the Anscombe data and theoretical line
_ = plt.plot(x,y, marker='.',linestyle='none')
_ = plt.plot(x_theor,y_theor)

# Label the axes
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()