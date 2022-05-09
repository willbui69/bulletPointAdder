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

# Using os.path to extract different parts of a path
filePath = Path.cwd()

# Get basename of the file
print(str(os.path.basename(filePath)))

# Get the root and parent path
print(str(os.path.dirname(filePath)))

# Get the dir name and base name together
print(str(filePath).split(os.sep))

# Get the size in bytes of the file
print(os.path.getsize(filePath))

# Get the list of file names
print(os.listdir(filePath))

# Get the total size of all files
totalSize = 0
for filename in os.listdir('/Users/mac/Desktop/python examples'):
    totalSize += os.path.getsize(os.path.join('/Users/mac/Desktop/python examples', filename))

print(totalSize)

# Modifying a list of files using glob patterns
p = Path('/Users/mac/Desktop')

print(list(p.glob('*.jpg')))

# Use * for multiple of any characters and ? for any single character
print(list(p.glob('*.??g')))

for imagefile in list(p.glob('*.??g')):
    print(imagefile)