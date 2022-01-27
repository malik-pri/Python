import sys
import os     # can use Pathlib module too
from PIL import Image

# convert JPG to PNG na store in new folder
# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)

# check if 'new/' exists, if not, create it.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through 'Pokedex/'
# convert images to png
# save to new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')



