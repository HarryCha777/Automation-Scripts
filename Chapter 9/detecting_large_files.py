#! python3
import os

print('Printing files with size over 100 MB...')

for folderName, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if os.path.getsize(os.path.join(folderName, filename)) > 100000:
            print(os.path.join(folderName, filename))

print('Done!')