# Import numpy and matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# Generate two 1-D arrays: u, v
u = np.linspace(-2, 2, 41)  # Generate 41 linear samples between -2 to 2
v = np.linspace(-1, 1, 21)

# Generate 2-D arrays from u and v: X, Y
X, Y = np.meshgrid(u, v)

# Compute Z based on X and Y
Z = np.sin(3 * np.sqrt(X ** 2 + Y ** 2))

# Display the resulting image with pcolor()
plt.pcolor(Z)
plt.show()

# Save the figure to 'sine_mesh.png'
# plt.savefig('sine_mesh.png')


# Generate a default contour map of the array Z
plt.subplot(2, 2, 1)
plt.contour(X, Y, Z)

# Generate a contour map with 20 contours
plt.subplot(2, 2, 2)
plt.contour(X, Y, Z, 20)

# Generate a default filled contour map of the array Z
plt.subplot(2, 2, 3)
plt.contourf(X, Y, Z)

# Generate a default filled contour map with 20 contours
plt.subplot(2, 2, 4)
plt.contourf(X, Y, Z, 20)

# Improve the spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()

# Create a filled contour plot with a color map of 'viridis'
plt.subplot(2, 2, 1)
plt.contourf(X, Y, Z, 20, cmap='viridis')
plt.colorbar()
plt.title('Viridis')

# Create a filled contour plot with a color map of 'gray'
plt.subplot(2, 2, 2)
plt.contourf(X, Y, Z, 20, cmap='gray')
plt.colorbar()
plt.title('Gray')

# Create a filled contour plot with a color map of 'autumn'
plt.subplot(2, 2, 3)
plt.contourf(X, Y, Z, 20, cmap='autumn')
plt.colorbar()
plt.title('Autumn')

# Create a filled contour plot with a color map of 'winter'
plt.subplot(2, 2, 4)
plt.contourf(X, Y, Z, 20, cmap='winter')
plt.colorbar()
plt.title('Winter')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()
