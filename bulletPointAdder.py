#! Python 3
# bulletPointAdder - A multipoint added program

import pyperclip
text = pyperclip.paste()
copiedText = text

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)

print(copiedText)


