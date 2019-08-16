#! python3
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
else:
    print('Options:')
    print('\"save [text]\":\t\t save the text')
    print('\"list\":\t\t\t copy the list of all saved texts')
    print('\"delete [text]\":\t delete the saved text')
    print('\"delete\":\t\t delete all saved texts')

mcbShelf.close()