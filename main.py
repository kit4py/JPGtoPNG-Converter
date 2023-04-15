# JPG to PNG converter
import sys
import os
from PIL import Image

print('''
       __               __           ____             
      / /___  ____ _   / /_____     / __ \____  ____ _
 __  / / __ \/ __ `/  / __/ __ \   / /_/ / __ \/ __ `/
/ /_/ / /_/ / /_/ /  / /_/ /_/ /  / ____/ / / / /_/ / 
\____/ .___/\__, /   \__/\____/  /_/   /_/ /_/\__, /  
    /_/    /____/                            /____/ 
''')


image_folder = sys.argv[1]
output_folder = sys.argv[2]
# image_folder1 = input('Folder name with images to convert: ')
image_folder = 'images/' + image_folder
# output_folder1 = input('Folder name with converted images: ')
output_folder = 'images/converted/' + output_folder
print('')

# check if folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# loop through folder
# convert images to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print('[+] img converted')

