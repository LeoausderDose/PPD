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
rotated_array = rotate(intensity_array, 2.5)

# Print the shape and intensity values of the array
print(f"Array shape: {intensity_array.shape}")
print(f"Array values: {intensity_array}")

print

# plt.imshow(rotated_array, cmap='hot', interpolation='nearest')
# plt.colorbar()
# plt.title('Intensity Heatmap')
# plt.show()