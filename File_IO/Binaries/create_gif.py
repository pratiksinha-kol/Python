# We are creating a GIF from a series of images.
# Import sys to handle command line arguments

import sys

# Ensure you have Pillow installed: 'pip install Pillow'
from PIL import Image

images = []

# Loop through all command line arguments (excluding the script name)
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Save the images as a GIF
# The first image is used as the base, and the rest are appended
# 'duration' sets the time each frame is displayed (in milliseconds)
# 'loop=0' means the GIF will loop indefinitely
images[0].save('output.gif',
               save_all=True,
               append_images=images[1:],
               duration=100,
               loop = 0)    