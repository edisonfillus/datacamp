import matplotlib.pyplot as plt
import numpy as np

# Load the image into an array: image
image = plt.imread('./data/Unequalized_Hawkes_Bay_NZ.jpg')

image = image.mean(axis=2)  # transform Black & White

# Display image in top subplot using color map 'gray'
plt.subplot(2, 1, 1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap='gray')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2, 1, 2)
plt.xlim((0, 255))
plt.hist(pixels, bins=64, range=(0, 256), normed=True, color='red', alpha=0.4)

# PDF = Probability Distribution Function
# CDF = Cumulative Distribution Function

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()

# Display a cumulative histogram of the pixels
plt.hist(pixels, bins=64, range=(0, 256),
               normed=True, cumulative=True,
               color='blue', alpha=0.4)

# Specify x-axis range, hide axes, add title and display plot
plt.xlim((0, 256))
plt.grid('off')
plt.title('PDF & CDF (original image)')

# Display the plot
plt.show()


# Generate a cumulative histogram
cdf, bins, patches = plt.hist(pixels, bins=256, range=(0,256), normed=True, cumulative=True)
new_pixels = np.interp(pixels, bins[:-1], cdf*255)

# Reshape new_pixels as a 2-D array: new_image
new_image = new_pixels.reshape(image.shape)

# Display the new image with 'gray' color map
plt.subplot(2,1,1)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image, cmap='gray')

# Generate a histogram of the new pixels
plt.subplot(2,1,2)
pdf = plt.hist(new_pixels, bins=64, range=(0,256), normed=False,
               color='red', alpha=0.4)
plt.grid('off')

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
plt.xlim((0,256))
plt.grid('off')

# Add title
plt.title('PDF & CDF (equalized image)')

# Generate a cumulative histogram of the new pixels
cdf = plt.hist(new_pixels, bins=64, range=(0,256),
               cumulative=True, normed=True,
               color='blue', alpha=0.4)
plt.show()
