#Password Authenticator 
import string
import random

#All functions to validate a password
class Validator: 
    #Takes in password as an argument
    def __init__(self, password):
        self.password = password

    #Verifies if the password contains 10 or more characters
    def checkLength(self):
        if(len(self.password) >= 10):
            length = True
        else: 
            length = False
        return length

    #Verifies if the password contains lowercase letters
    def checkLower(self):
        lower = any(x.islower() for x in self.password)
        return lower

    #Verifies if the password contains uppercase letters
    def checkUpper(self):
        upper = any(x.isupper() for x in self.password)
        return upper

    #Verifies if the password contains numbers
    def checkDigit(self):
        digit = any(x.isdigit() for x in self.password)
        return digit

    #Verifies if the password contains special characters
    def checkSpecial(self):
        specialChars = set(string.punctuation)
        special = any(char in specialChars for char in self.password)
        return special

    #Validates the password given the criteria 
    def validate(self):
        length = self.checkLength()
        lower = self.checkLower()
        upper = self.checkUpper()
        digit = self.checkDigit()
        special = self.checkSpecial()

        report = length and lower and upper and digit and special
        if report:
            print('Your password is VALID.')
        elif not length:
            print('Your password needs to be more than 10 characters.')
            return False
        elif not lower: 
            print('Your password needs to have at least 1 lowercase letter.')
            return False
        elif not upper:
            print('Your password needs to have at least 1 uppercase letter.')
            return False
        elif not digit:
            print('Your password needs to have at least 1 number.')
            return False
        elif not special:
            print('Your password needs to have at least 1 special character.')
        else:
            pass

#Main with password generator
while True: 
    print('Would you like to validate an existing password or generate a new one?')
    userInput = input('Type "Validate" or "Generate": ')
    userInput = userInput.upper()

    if(userInput == 'GENERATE'): 
        #Randomly chooses 6 characters from lowercase letters
        def lowerGen(size = 6, chars = string.ascii_lowercase):
            return ''.join(random.choice(chars) for _ in range(size))
        
        #Randomly chooses an uppercase letter
        def upperGen(chars = string.ascii_uppercase):
            return ''.join(random.choice(chars))

        #Randomly chooses 2 numbers
        def digitGen(size = 2, chars = string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        #Randomly chooses a special character
        def specialGen(chars = string.punctuation):
            return ''.join(random.choice(chars))
        
        #Concantenates the strings
        print('Generated Password: ' + specialGen() + upperGen() + lowerGen() + digitGen())

    #Validates password    
    elif(userInput == 'VALIDATE'):
        userPass = input('Enter Password: ')
        x = Validator(userPass)
        x.validate()

    #Ends program due to incorrect input
    else:
        print('ERROR. Incorrect Input.')
        break

    #Runs again
    runAgain = input('Would you like to run Password Authenticator again? (Y/N): ')
    runAgain = runAgain.upper()
    if(runAgain != 'Y'):
        break



