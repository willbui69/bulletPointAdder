#! Python3
#pigLatin.py - A program that alters English words

#vowels
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

#Ask user for the text to alter
print("Type the text you want to change:")
originalText = input()

#Check the user input
if not len(originalText.strip()):
    print('Text must not be empty or just spaces') 

#Split the text into words
originalWords = originalText.split()

#Alter each word as requested
for i, word in enumerate(originalWords):

    #if words start with a vowel
    if word[0].lower() in VOWELS:

        #In case characters are all alpha
        if word.isalpha():
            word = word + 'yay'
            originalWords[i] = word
        
        #In case the ending word has special signs
        else:
            word = word[0:len(word)-1] + 'yay' + word[-1]
            print(word)
            originalWords[i] = word

    #Check if word starts with sw
    elif word.lower().startswith('sw'):
        word = word[2:-1] + word[0:2] + 'ay'
        originalWords[i] = word

    #Check all characters just digits and letters
    elif word.isalnum():
        word = word[1:len(word)] + word[0] + 'ay'
        originalWords[i] = word

    #Keep the word as original like numbers or special characters
    else:
         originalWords[i] = word   

#Join all words together
newText = ' '.join(originalWords)

#Print the new text on the screen
print(newText)