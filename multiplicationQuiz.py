### A Multiplication Quizzes Program

# Import pyinputplus module for input validation
from socket import timeout
import pyinputplus as pyip

# Import random, time modules
import random, time

# Set the number of questions and correct answers
numOfQuizzes = 10
correctAnswers = 0

# Loop through all the questions
for quizNumber in range(numOfQuizzes):
    # Pick two random numbers from 0 to 9
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    # A prompt to user
    prompt = '#%s: %s * %s = ' % (quizNumber, num1, num2)

    try:
        pyip.inputStr(prompt, allowRegexes = ['%s' % (num1 * num2)],
                             blockRegexes = [('.*', 'Incorrect!')],
                             timeout = 10, limit = 2)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    
    else:
        print('Correct!')
        correctAnswers += 1
    
    time.sleep(1)

print('Score: %s / %s' % (correctAnswers, numOfQuizzes))