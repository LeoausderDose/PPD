import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import rotate

def import_tif_image(filepath):
    # Open the TIFF image using PIL
    image = Image.open(filepath)

    # Convert the image to grayscale if it's not already
    image = image.convert('L')

    # Convert the PIL image to a NumPy array
    array = np.array(image)

    return array

# Example usage
tif_filepath = 'LSC_nopinhole_40ms_100_1_MMStack_Pos0.ome.tif'
intensity_array = import_tif_image(tif_filepath)

# Rotate the intensity array by 2.5 degrees counterclockwise
rotated_array = rotate(intensity_array, 2.5)

# Create a heatmap plot of the rotated intensity array
plt.imshow(rotated_array, cmap='hot', interpolation='nearest')

# Remove ticks on x and y axes
plt.xticks([])
plt.yticks([])

# Add a colorbar with a label
cbar = plt.colorbar(label='Intensity')

# Add a scale bar
scale_bar_length = 100  # Modify this value as needed
scale_bar_units = 'pixels'  # Modify this value as needed
scale_bar_x = 1300  # x-coordinate of the scale bar
scale_bar_y = 1050  # y-coordinate of the scale bar
plt.plot([scale_bar_x, scale_bar_x + scale_bar_length], [scale_bar_y, scale_bar_y], color='white', linewidth=2)
plt.text(scale_bar_x + scale_bar_length / 2, scale_bar_y - 30, f'{scale_bar_length} {scale_bar_units}', ha='center', color='white')

# Set plot title and adjust layout
plt.title('Intensity Heatmap')
plt.tight_layout()

# Display the plot
plt.show()
