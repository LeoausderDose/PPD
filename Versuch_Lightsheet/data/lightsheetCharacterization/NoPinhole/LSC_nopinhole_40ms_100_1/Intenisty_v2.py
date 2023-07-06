import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import rotate
from scipy.optimize import curve_fit

def import_tif_image(filepath):
    # Open the TIFF image using PIL
    image = Image.open(filepath)

    # Convert the image to grayscale if it's not already
    image = image.convert('L')

    # Convert the PIL image to a NumPy array
    array = np.array(image)

    return array

def two_gaussian(x, A1, x0_1, sigma1, A2, x0_2, sigma2):
    return A1 * np.exp(-(x - x0_1) ** 2 / (2 * sigma1 ** 2)) + A2 * np.exp(-(x - x0_2) ** 2 / (2 * sigma2 ** 2))


# Example usage
tif_filepath = 'LSC_nopinhole_40ms_100_1_MMStack_Pos0.ome.tif'
intensity_array = import_tif_image(tif_filepath)

# Rotate the intensity array by 90 degrees counterclockwise
rotated_array = rotate(intensity_array, 2.5)


# Generate two cuts for fits

yslice = rotated_array[:,750]
xslice = rotated_array[600,:]

# # Initial parameter guesses for the Gaussian fit
# initial_params = [np.max(data), np.argmax(data) % rotated_array.shape[1], 1.0,
#                   np.max(data), np.argmax(data) // rotated_array.shape[1], 1.0]

# # Perform the curve fit
# fit_params, _ = curve_fit(two_gaussian, (X, Y), data, p0=initial_params)

# # Generate the fitted surface using the fit parameters
# fitted_data = two_gaussian((X, Y), *fit_params).reshape(rotated_array.shape)

# # Create a heatmap plot of the rotated intensity array and the fitted surface
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# ax1.imshow(rotated_array, cmap='hot', interpolation='nearest')
# ax1.set_title('Rotated Intensity Heatmap')

# ax2.imshow(fitted_data, cmap='hot', interpolation='nearest')
# ax2.set_title('Fitted Surface')


# Create a heatmap plot of the rotated intensity array
plt.imshow(rotated_array, cmap='hot', interpolation='nearest')

# Add a colorbar with a label
cbar = plt.colorbar()
cbar.set_label('Intensity')

# Add a scale bar
scale_bar_length = 100  # Modify this value as needed
scale_bar_units = 'pixels'  # Modify this value as needed
scale_bar_x = 1300  # x-coordinate of the scale bar (fraction of the plot width)
scale_bar_y = 1050  # y-coordinate of the scale bar (fraction of the plot height)
plt.plot([scale_bar_x, scale_bar_x + scale_bar_length], [scale_bar_y, scale_bar_y], color='white', linewidth=2)
plt.text(scale_bar_x + scale_bar_length / 2, scale_bar_y - 30, f'Lenght', ha='center', color = 'white')


# Create colorbar

# plt.colorbar()
plt.title('Intensity Heatmap')

plt.tight_layout()
plt.show()
