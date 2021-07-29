#Password Authenticator 
import string
import random

class Validator: 
    def __init__(self, password):
        self.password = password

    def checkLength(self):
        if(len(self.password) >= 10):
            length = True
        else: 
            length = False
        return length
        
    def checkLower(self):
        lower = any(x.islower() for x in self.password)
        return lower

    def checkUpper(self):
        upper = any(x.isupper() for x in self.password)
        return upper

    def checkDigit(self):
        digit = any(x.isdigit() for x in self.password)
        return digit

    def checkSpecial(self):
        specialChars = set(string.punctuation)
        special = any(char in specialChars for char in self.password)
        return special

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

while True: 
    print('Would you like to validate an existing password or generate a new one?')
    userInput = input('Type "Validate" or "Generate": ')
    userInput = userInput.upper()

    if(userInput == 'GENERATE'): 
        def lowerGen(size = 6, chars = string.ascii_lowercase):
            return ''.join(random.choice(chars) for _ in range(size))
        
        def upperGen(chars = string.ascii_uppercase):
            return ''.join(random.choice(chars))

        def digitGen(size = 2, chars = string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        def specialGen(chars = string.punctuation):
            return ''.join(random.choice(chars))

        print('Generated Password: ' + specialGen() + upperGen() + lowerGen() + digitGen())
    elif(userInput == 'VALIDATE'):
        userPass = input('Enter Password: ')
        x = Validator(userPass)
        x.validate()
    else:
        print('ERROR. Incorrect Input.')
        break

    runAgain = input('Would you like to run Password Authenticator again? (Y/N): ')
    runAgain = runAgain.upper()
    if(runAgain != 'Y'):
        break



    




