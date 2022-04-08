import re

#Find phone number with regex
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is (415)-555-4242.')

print('Phone number found: ' + mo.group(1))

#Use parentheses to create groups  in regex
print(mo.group(2))
print(mo.group())
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode, mainNumber)

#Use the pipe(|) to match multiple groups
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')

print(mo1.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo2 = batRegex.search('Batmobile lost a wheel')

print(mo2.group(1))

#Optional Matching with question mark
batRegex2 = re.compile(r'Bat(wo)?man')
mo3 = batRegex2.search('The Adventures of Batman')
print(mo3.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4 = phoneRegex.search('My number is 555-4242')
print(mo4.group())

#Matching zero or more with stars
batRegex3 = re.compile(r'Bat(wo)*man')
mo5 = batRegex3.search('The Adventures of Batman')
print(mo5.group())

mo6 = batRegex3.search('The Adventures of Batwoman')
print(mo6.group())

mo7 = batRegex3.search('The Adventures of Batwowowowoman')
print(mo7.group())

#Matching one or more with the Plus
batRegex4 = re.compile(r'Bat(wo)+man')
mo8 = batRegex4.search('The Adventures of Batwowowowoman')
print(mo8.group())

# mo9 = batRegex4.search('The Adventures of Batman')
# print(mo9.group())

#Matching specific repititions with braces
haRegex = re.compile(r'(Ha){0,5}')
mo10 = haRegex.search('HaHaHaHaHa')
mo11 = haRegex.search('Ha I don\'t care')
print(mo10.group())
print(mo11.group())

#Non-greedy Matching
haRegex1 = re.compile(r'(Ha){3,5}?')
mo12 = haRegex1.search('HaHaHaHaHa')
print(mo12.group())

#Findall method without groups  will return a list
phoneNumReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo13 = phoneNumReg.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo13)

#Findall method with groups will return a list of tuples
phoneNumReg1 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo14 = phoneNumReg1.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo14)