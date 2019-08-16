#! python3
import os, shutil

print('Creating Folder-of-Copied-Files if it does not exist...')

workingDirPath = os.path.abspath('.')
folderOfCopiedFilesPath = os.path.join(workingDirPath, 'Folder-of-Copied-Files')
if not os.path.exists(folderOfCopiedFilesPath):
    os.mkdir(folderOfCopiedFilesPath)
    
print('Note that this program only detects from its current folder and not from any of its subfolders.')
print('Detecting and copying PDF and JPG files to Folder-of-Copied-Files...')

for filename in os.listdir('.'):
    if filename.endswith('.pdf') or filename.endswith('.jpg'):
        filePath = os.path.join(workingDirPath, filename)
        copiedFilePath = os.path.join(folderOfCopiedFilesPath, filename)
        shutil.copy(filePath, copiedFilePath)

print('Done!')