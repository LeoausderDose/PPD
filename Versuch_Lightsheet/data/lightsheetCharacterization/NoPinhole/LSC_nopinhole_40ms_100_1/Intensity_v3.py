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

def get_max_index(array):
    # Flatten the array to a 1D array
    flattened_array = array.flatten()
    
    # Find the index of the maximum value in the flattened array
    max_index = np.argmax(flattened_array)
    
    # Convert the index to 2D coordinates
    max_row = max_index // array.shape[1]
    max_col = max_index % array.shape[1]
    
    return (max_row, max_col)

def gaussian_function(x, amplitude, mean, std_dev):
    """
    Gaussian function with parameters amplitude, mean, and standard deviation.
    """
    return amplitude * np.exp(-(x - mean)**2 / (2 * std_dev**2))


# Example usage
tif_filepath = 'Versuch_Lightsheet/data/lightsheetCharacterization/NoPinhole/LSC_nopinhole_40ms_100_1/LSC_nopinhole_40ms_100_1_MMStack_Pos0.ome.tif'
intensity_array = import_tif_image(tif_filepath)

# Rotate the intensity array by 2.5 degrees counterclockwise
rotated_array = rotate(intensity_array, 2.5)

# Find Index of Maxima and create slices

max_index = get_max_index(rotated_array)
print(max_index)
xslice = rotated_array[max_index[0],:]
yslice = rotated_array[:,max_index[1]]

# Fit the Gaussian to the data
initial_guess_x = [80, max_index[0], 130]  # Initial guess for the parameters
params_x, params_covariance_x = curve_fit(gaussian_function, range(len(xslice)), xslice, p0=initial_guess_x)
print(params_x)

initial_guess_y = [80, max_index[1], 30]  # Initial guess for the parameters
params_y, params_covariance_y = curve_fit(gaussian_function, range(len(yslice)), yslice, p0=initial_guess_y)
print(params_y)



# Create a heatmap plot of the rotated intensity array
scopef = 3
plt.imshow(rotated_array, cmap='hot', interpolation='nearest')   #[:,int(params_x[1]-scopef*params_x[2]):int(params_x[1]+scopef*params_x[2])], cmap='hot', interpolation='nearest')

# Remove ticks on x and y axes

# plt.xticks([])
# plt.yticks([])

# Add a colorbar with a label


cbar = plt.colorbar(label='Intensity',location = 'bottom')

# Add a scale bar


scale_bar_length = 100  # Modify this value as needed
scale_bar_units = 'pixels'  # Modify this value as needed
scale_bar_x = 850  # x-coordinate of the scale bar
scale_bar_y = 750  # y-coordinate of the scale bar
plt.plot([scale_bar_x, scale_bar_x + scale_bar_length], [scale_bar_y, scale_bar_y], color='white', linewidth=2)
plt.text(scale_bar_x + scale_bar_length / 2, scale_bar_y - 30, f'{scale_bar_length} {scale_bar_units}', ha='center', color='white')

# Set plot title and adjust layout
#plt.title('Intensity Heatmap')
plt.tight_layout()

# Display the plot
plt.show()
