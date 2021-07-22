#NOTES 
#.join combines the characters without commas and ""
#The join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator
#The string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation are pre-existing lists for alphabetical letters, numbers, and punctuations 

import string
import random

print("A strong and secure password consists of a combination of special characters, lowercase and uppercase characters, numbers, and a minimum of ten total characters.")


while True:
    userInput = input("Generate strong and secure password? (Y/N): ")
    userInput = userInput.upper()
    if(userInput != "Y"): 
        break
    else:
        #Takes in max of 6 characters and stores lowercase letters into variable chars 
        def lowercaseGenerator(size = 6, chars = string.ascii_lowercase): 
            return ''.join(random.choice(chars) for _ in range(size))

        #Takes one character and stores uppercase letters into variable chars
        def uppercaseGenerator(chars = string.ascii_uppercase):
            return ''.join(random.choice(chars))

        #Takes in max of 2 characters and stores numbers into variable chars
        def numberGenerator(size = 2, chars = string.digits):
            return ''.join(random.choice(chars) for _ in range(size))
            
        #Takes one character and stores punctuation into variable chars
        def specialCharGenerator(chars = string.punctuation):
            return ''.join(random.choice(chars))
            
        print(specialCharGenerator() + uppercaseGenerator() + lowercaseGenerator() + numberGenerator ())

    runAgain = input("Would you like to run Password Generator Again? (Y/N): ")
    runAgain = runAgain.upper()
    if(runAgain != "Y"):
        break



