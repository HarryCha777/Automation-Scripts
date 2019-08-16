![automate boring stuff image](https://user-images.githubusercontent.com/36347727/63128254-7ae51d00-bf82-11e9-9956-dcbaaab745b5.jpg)

# Automation-Scripts

These are my Python solutions to practice projects listed in the book Automate the Boring Stuff by Al Sweigart.

All solutions in this repository are functional and may be practical.

Example: Chapter 13: PDF Paranoia - Encrypts all PDF files, checks their confidentiality, and then trashes the original unencrypted PDF files.
```javascript
#! python3
import PyPDF2, os, send2trash

password = input('Please enter the password to encrypt all unencrypted PDF files:\n')

print('Finding all unencrypted PDF files and encrypting them...')
for folderName, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            originalPdf = open(os.path.join(folderName, filename), 'rb')
            pdfReader = PyPDF2.PdfFileReader(originalPdf)
            if not pdfReader.isEncrypted:
                print(os.path.join(folderName, filename) + ' is an unencrypted PDF file. Encrypting it...')
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.encrypt(password)
                resultPdf = open(filename + '_Encrypted.pdf', 'wb')
                pdfWriter.write(resultPdf)
                originalPdf.close() # Close the original PDF files here since else, they cannot be trashed later since they are used by this process.
                resultPdf.close()

print()
print('Checking if all PDF files are encrypted with the provided password...')
allEncrypted = True
for folderName, subfolders, filenames in os.walk('.'):
    for filename in filenames:    
        if filename.endswith('_Encrypted.pdf'):
            resultPdf = open(os.path.join(folderName, filename), 'rb')
            pdfReader = PyPDF2.PdfFileReader(resultPdf)
            print('Checking ' + os.path.join(folderName, filename) + ' ...')
            if not pdfReader.decrypt(password):
                allEncrypted = False
                print(os.path.join(folderName, filename) + ' is not encrypted with the provided password!')                
            resultPdf.close()
        elif filename.endswith('.pdf'): # the original unencrypted PDF to trash.
            print('Trashing ' + os.path.join(os.path.abspath(folderName)) + ' ...')
            send2trash.send2trash(os.path.join(os.path.abspath(folderName)))

if allEncrypted:
    print('All PDF files are encrypted with the provided password!')
else:
    print('Not all PDF files are encrypted with the provided password.')
    print('This may be because some PDF files with ending \"_Encrypted.pdf\" were already encrypted with a different password before this program was launched.')

print('Done!')
```
---

Link to Automate the Boring Stuff: http://automatetheboringstuff.com

# Contact
Please reach out to me through this email address:    harrycha777@gmail.com

# License
This project is under no license.
