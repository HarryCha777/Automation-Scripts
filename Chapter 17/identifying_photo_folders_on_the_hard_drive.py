#! python3
import os
from PIL import Image

print('Detecting folders with half or more of their contents as PNG or JPG files with size over 500 x 500 pixels...')

noneFound = True
for foldername, subfolders, filenames in os.walk('.'):
    numPhotoFiles = numNonPhotoFiles = 0
    for filename in filenames:
        if not filename.endswith('.png') and not filename.endswith('.jpg'):
            numNonPhotoFiles += 1
            continue

        fileImage = Image.open(os.path.join(foldername, filename))
        width, height = fileImage.size

        if width > 500 and height > 500:
            numPhotoFiles += 1
        else:
            numNonPhotoFiles += 1

    if numPhotoFiles > numNonPhotoFiles:
        noneFound = False
        print(os.path.abspath(foldername))

if noneFound:
    print('No photo folder found!')
print('Done!')