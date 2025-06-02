#Read the image
from tifffile import imread, imsave, imwrite
import numpy as np
pathfile=
savefile=
img = imread(pathfile)

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
# convert back to save
img = img.astype(np.uint16)  

# Save corrected image
imwrite(savefile, img, imagej=True)
