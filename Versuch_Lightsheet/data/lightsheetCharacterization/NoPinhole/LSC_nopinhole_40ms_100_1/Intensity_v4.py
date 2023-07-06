import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import rotate
from scipy.optimize import curve_fit

def import_tif_image(filepath):
    image = Image.open(filepath)
    image = image.convert('L')
    array = np.array(image)
    return array

def get_max_index(array):
    flattened_array = array.flatten()
    max_index = np.argmax(flattened_array)
    max_row = max_index // array.shape[1]
    max_col = max_index % array.shape[1]
    return (max_row, max_col)

def gaussian_function(x, amplitude, mean, std_dev):
    return amplitude * np.exp(-(x - mean)**2 / (2 * std_dev**2))


tif_filepath = 'Versuch_Lightsheet/data/lightsheetCharacterization/NoPinhole/LSC_nopinhole_40ms_100_1/LSC_nopinhole_40ms_100_1_MMStack_Pos0.ome.tif'
intensity_array = import_tif_image(tif_filepath)

rotated_array = rotate(intensity_array, 2.5)

max_index = get_max_index(rotated_array)
print(max_index)

xslice = rotated_array[max_index[0], :]
yslice = rotated_array[:, max_index[1]]

initial_guess_x = [80, max_index[0], 130]
params_x, params_covariance_x = curve_fit(gaussian_function, range(len(xslice)), xslice, p0=initial_guess_x)
print(params_x)

initial_guess_y = [80, max_index[1], 30]
params_y, params_covariance_y = curve_fit(gaussian_function, range(len(yslice)), yslice, p0=initial_guess_y)
print(params_y)

scopef = 3

plt.imshow(rotated_array, cmap='hot', interpolation='nearest')
cbar = plt.colorbar(label='Intensity', location='bottom', shrink=.79, pad=0.02)

scale_bar_length = 100
scale_bar_units = 'pixels'
scale_bar_x = 850
scale_bar_y = 750
plt.plot([scale_bar_x, scale_bar_x + scale_bar_length], [scale_bar_y, scale_bar_y], color='white', linewidth=2)
plt.text(scale_bar_x + scale_bar_length / 2, scale_bar_y - 20, f'{scale_bar_length} {scale_bar_units}', ha='center', color='white')

plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()
