#! python3
import openpyxl
from openpyxl.styles import Font

num = input('Please input the size of the multiplication table (a number between 1 and 25 inclusive):\n')

print('Creating the excel file...')
wb = openpyxl.Workbook()

sheet = wb.active
sheet.title = 'Multiplication Table'

print('Filling in the excel file...')
bold14 = Font(size=14, bold=True)
for i in range(int(num)):
    sheet[chr(ord('A') + i + 1) + '1'].font = bold14
    sheet[chr(ord('A') + i + 1) + '1'] = i + 1
for i in range(int(num)):
    sheet['A' + str(i + 2)].font = bold14
    sheet['A' + str(i + 2)] = i + 1
for i in range(int(num)):
    for j in range(int(num)):
        sheet[chr(ord('B') + i) + str(j + 2)] = (i+1) * (j+1)

wb.save('excel_multiplication_table.xlsx')
print('Done!')