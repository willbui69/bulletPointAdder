import re

# function that matches a string that has an a followed by zero or more b's
def checkStringMatch(string):
    stringRex = re.compile(r'^a(b)*$')
    string = stringRex.search(string)
    return bool(string)

print(checkStringMatch('abc'))

#function to check a string that has an a followed by one or more b's
def checkStrinngMatch1(string):
    stringRex = re.compile(r'^a(b)+')
    string = stringRex.search(string)
    return bool(string)

print(checkStrinngMatch1('abbbbbbccc'))

#function to check a string that has an a followed by zero or one b's
def checkStringMatch2(string):
    stringRex = re.compile(r'^a(b)?')
    string = stringRex.search(string)
    return bool(string)

print(checkStringMatch2('abbb0dddd'))

#function to check a string that has an a followed by zero or one b
def checkStringMatch3(string):
    stringRex = re.compile(r'ab?')
    string = stringRex.search(string)
    return bool(string)

print(checkStringMatch3('abb'))

#function to check a string that has an a followed by three b
def checkStringMatch4(string):
    stringRex = re.compile(r'a(b){3}?')
    string = stringRex.search(string)
    return bool(string)

print(checkStringMatch4('abbbcd'))

#function to check a string that has an a followed by two to three b
def checkStringMatch5(string):
    stringRex = re.compile(r'ab{2,3}')
    string = stringRex.search(string)
    return bool(string)

print(checkStringMatch5('cdabbda'))

#function to find the sequences of lowercase letters joined with a underscore
def checkStringMatch6(string):
    stringRex = re.compile(r'[a-z]+_[a-z]+$')
    string = stringRex.findall(string)
    return string

print(checkStringMatch6('Aaab_vBBalkdjf_dd'))

#function to find the sequences of one uppercase followed by lowercase letters
def checkStringMatch7(string):
    stringRex = re.compile(r'[A-Z]?[a-z]+') 
    string = stringRex.findall(string)
    return string

print(checkStringMatch7('AAacdBbGg'))
print(checkStringMatch7('Python'))

#function to check a string that has an 'a' followed anything and ending in 'b'
def checkStringMatch8(string):
    stringRex = re.compile(r'a.*b$')
    string = stringRex.findall(string)
    return string

print(checkStringMatch8('Vdkfdie339fjb'))

#function to check a string to match a word at the beginning
def checkStringMatch9(string):
    stringRex = re.compile(r'^\w+')
    string = stringRex.search(string)
    return bool(string)

print(checkStringMatch9('ddkdkd dww'))

# Function to check a string to match a word at the end, with optional punctuation
def checkStringMatch10(string):
    stringRex = re.compile(r'\w+\S*$')
    string = stringRex.search(string)
    return bool(string)

print(checkStringMatch10('.'))

# Function to find words containing 'z'
def checkStringMatch11(string):
    stringRex = re.compile(r'\w*z.\w*')
    words = stringRex.findall(string)
    return words

print(checkStringMatch11('zoombie tingzo haoki'))

# Function to find words containing 'z' not at the start nor the end
def checkStringMatch12(string):
    stringRex = re.compile(r'\w*\Bz\B\w*')
    words = stringRex.findall(string)
    return words

print(checkStringMatch12("The zoombie and a quick brown fox jumps over the lazy dog."))

# Function to find strings that contains only upper and lowercase letters, numbers and underscores
def checkStringMatch13(string):
    stringRex = re.compile(r'^[a-zA-Z0-9_]*$')
    string = stringRex.findall(string)
    return string

print(checkStringMatch13("Python_Exercises_1"))

# Function to find string starting with a specific number
def findStringMatch(string):
    stringRex = re.compile(r'\d+.+')
    string = stringRex.findall(string)
    return string

print(findStringMatch("dkgg 8ddkg 4dd"))

#Function to remove leading zeors from an IP address
def removeZero(string):
    zeroReg = re.compile('0')
    string = zeroReg.sub('',string)
    return string

print(removeZero("190.168.10.05"))

# Function to check for a number at the end of a string
def findStringMatch1(string):
    stringRex = re.compile(r'.*[0-9]$')
    string = stringRex.findall(string)
    return bool(string)

print(findStringMatch1("kdf3 eee2kkl 1kdd3"))

# Function to search numbers of length between 1 to 3 in a given string
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))

# Function to search some literals strings in a string
def searchLiteralString(string, searchedword):
    stringRex = re.compile(searchedword)
    string = stringRex.search(string)
    if string != None:
        return True
    else:
        return False

print(searchLiteralString('The quick brown fox jumps over the lazy dog.', 'dog'))

# Function to search some literals strings in a string
patterns = ['fox', 'dog', 'horse']
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' %(pattern, text))
    if re.search(pattern, text):
        print('Matched!')
    else:
        print('Not Matched!')

# Function to search a literals string in a string and its location
def searchLocationString(string, searchedWord):
    stringRex = re.compile(searchedWord)
    match = stringRex.search(string)
    print('Found "%s" in "%s" from %d to %d ' % (searchedWord, string, match.start(), match.end()))

searchLocationString('The quick brown fox jumps over the lazy dog.','fox')

# Function to find substrings within a string
def findSubString(string,subString):
    stringRex = re.compile(subString)
    matches = stringRex.findall(string)
    for match in matches:
        print(match)

findSubString('Python exercises, PHP exercises, C# exercises', 'exercises')

# Function to find the occurrence and position of substrings within a string
def findOccurrence(string, subString):
    matches = re.finditer(subString, string)
    for match in matches:
        s = match.start()
        e = match.end()
        print('Found %s at %d:%d' %(subString, s, e))

findOccurrence('Python exercises, PHP exercises, C# exercises','exercises')

# Function to replace whitespaces with an underscore
def replaceWhitespace(string):
    charRex = re.compile(r'[ ]')
    string = charRex.sub('_', string)
    print(string)

replaceWhitespace('he quick brown_fox_jumps_over the_lazy dog.')

# Function to replace underscores with whitespace
def replaceUnderscore(string):
    string = string.replace("_", " ")
    print(string)

replaceUnderscore("The_quick_brown_fox_jumps_over_the_lazy_dog.")

# Function to extract year, month and date from an url
def extractDate(url):
    return re.findall(r'/(\d{4}/(\d{1,2})/(\d{1,2}))', url)

print(extractDate("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/")[0][0])
