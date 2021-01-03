# ! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage :   py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#           py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

# Copying and pasting will require the pyperclip module, and reading the command line arguments will require the sys module. The shelve mod- ule will also come in handy: Whenever the user wants to save a new piece of clipboard text, you’ll save it to a shelf file. Then, when the user wants to paste the text back to their clipboard, you’ll open the shelf file and load it back into your program.

mcbShelf = shelve.open('mcb')

#TODO1 : Save clipboard content.

if len(sys.argv) == 3 and sys.argv[1].lower()== 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #TODO2 : List keywords and load content.
    if sys.argv[1].lower() == 'list': #a string representation of the list of shelf keys will be copied to the clipboard
        pyperclip.copy(str(list(mcbShelf.keys()))) #The user can paste this list into an open text editor to read it.
    elif sys.argv[1] in mcbShelf: #Otherwise, you can assume the command line argument is a keyword. If this keyword exists in the mcbShelf shelf as a key, you can load the value onto the clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()