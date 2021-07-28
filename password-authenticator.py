# NOTES
# The .join command combines the characters without commas and ""
# The join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator
# The string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation are pre-existing lists for alphabetical letters, numbers, and punctuations 
# import timeit inserts a timer
# import string for ascii

import string
import random

print('Choose from Menu:')
print('To Generate a Strong Password, Enter "G": ')
print('To Validate an Existing Password, Enter "V": ')

while True:
    userInput = input('Enter Your Choice: ')
    userInput = userInput.upper()
    if(userInput != 'V'): 
        break
    else:
        #Generate strong password
        if(userInput == 'G'):
            # Takes in max of 6 characters and stores lowercase letters into variable chars 
            def lowercaseGenerator(size = 6, chars = string.ascii_lowercase): 
                return ''.join(random.choice(chars) for _ in range(size))

            # Takes one character and stores uppercase letters into variable chars
            def uppercaseGenerator(chars = string.ascii_uppercase):
                return ''.join(random.choice(chars))

            # Takes in max of 2 characters and stores numbers into variable chars
            def numberGenerator(size = 2, chars = string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
                
            # Takes one character and stores punctuation into variable chars
            def specialCharGenerator(chars = string.punctuation):
                return ''.join(random.choice(chars))
                
            print(specialCharGenerator() + uppercaseGenerator() + lowercaseGenerator() + numberGenerator ())

        #Validate existing password
        else: 
            #A password should be 8 characters or more = 2pts
            #A password should include lowercase characters = 2pts
            #A password should include uppercase characters = 2pts
            #A password should include numbers = 2pts 
            #A password should include special characters = 2pts 
            #A password shouldn’t be the word “password” or the same letter or number repeated = 2pts
            #Total points: 10pts
            count = 0
            strengthList = ['Very Weak', 'Weak', 'Moderate', 'Strong', 'Unhackable']
            existingPassword = input('Enter an Existing Password: ')
            existingPassword = str(existingPassword)
            if(len(existingPassword) >= 16):
                count = count + 2
            if(all(existingPassword) in string.ascii_lowercase):
                count = count + 2
            if(all(existingPassword) in string.ascii_uppercase):
                count = count + 2
            if(all(existingPassword) in string.digits):
                count = count + 2
            if(all(existingPassword) in string.punctuation):
                count = count + 2
            if('password', 'Password' in existingPassword):
                count = count - 2
            
            if(count < 1):
                print(strengthList[0])
            elif(count < 3): 
                print(strengthList[1])
            elif(count < 5):
                print(strengthList[2])
            elif(count < 7):
                print(strengthList[3])
            elif(count < 10):
                print(strengthList[4]) 


    runAgain = input('Would you like to run Password Generator Again? (Y/N): ')
    runAgain = runAgain.upper()
    if(runAgain != 'Y'):
        break
    




