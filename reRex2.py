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

print(checkStringMatch9(' 2ddkdkd'))

