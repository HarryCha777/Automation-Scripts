#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print('Printing the list of lists with each column right-justified.')

for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print(tableData[j][i].rjust(10), end='')
    print()

print('Done!')