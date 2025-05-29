from tifffile import imread, imsave
import os

# Define input and output files
input_file = os.path.join("example_data", "A2-green.tif")
output_file = os.path.join("example_data", "A2-green_corrected.tif")

# Read the image
img = imread(input_file)

# Separate channels (assuming: 0 = BF, 1 = Green, 2 = Red)
# No cal usar-les si no les modifies individualment
Bkg_green = 0
Bkg_red = 0

# Subtract background
img[:, 1, :, :] -= Bkg_green
img[:, 2, :, :] -= Bkg_red

# Clamp negative values to zero
img[img < 0] = 0

# Save corrected image
imsave(output_file, img)
