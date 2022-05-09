from pathlib import Path, PosixPath, WindowsPath

myFiles = ['accounts.txt', 'detail.csv', 'invite.docx']

for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))

#Path('spam') / 'bacon' / 'egg'
# PosixPath('spam/bacon/eggs')
# Path('spam') / Path('bacon', 'eggs')

homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')
homeFolder / subFolder

PosixPath('C:/Users/Al/spam')

str(homeFolder / subFolder)

import os
# Get current working directory path with Path.cwd
print(Path.cwd())

# Get home directory with Path.home
print(Path.home())

# Create new folder with os.makedirs()
#os.makedirs('delicious\\walnut\\walfles')

# Convert a relative path into absolute path
print(os.path.abspath('.'))

# Check whether a path is an absolute path
print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))

# Extract atrribute from the file path
p = Path('/Users/mac/Desktop/python examples/mclip.py')

# Get root folder of the filesystem
print(p.anchor)

# Get parent folder that contains the file
print(p.parent)

# Get the file
print(p.name)

# Get the name of the file
print(p.stem)

# Get suffix (extension)
print(p.suffix)

print(Path.cwd())

print(Path.cwd().parents[0])

print(Path.cwd().parents[1])

print(Path.cwd().parents[2])

print(Path.cwd().parents[3])


