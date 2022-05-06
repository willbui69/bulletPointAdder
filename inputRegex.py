import pyinputplus as pyip

number = pyip.inputRegex(r'^\w{6}$', prompt="Confirmation number: ").upper()

print(number)