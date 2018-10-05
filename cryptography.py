"""
cryptography.py
Author: Joe Richter
Credit: https://www.codementor.io/python/tutorial/python-encryption-message-in-python-via-reverse-cipher

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
import string
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
straight = {}
reverse = {}
for j in range(0, len(associations)):
    straight[associations[j]] = j
    reverse[j] = associations[j]
Question = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
if Question == "e":
    enput = str(input("Message:"))
    enkey = str(input("Key: "))
    outputen = ""
    listput = list(enput)
    listkey = list(enkey)
    j = 0
    while len(enput) > len(enkey):
        enkey += enkey[j]
        j += 1
    for o in range(0, len(enput)):
        if straight[enput[o]] + straight[enkey[o]] <= len(associations):
                outputen += reverse[straight[enput[o]]] + straight[enkey[o]]
        else:
            outputen += reverse[straight[enput[o]] + straight[enkey[o]] = (len(associations))
    print(outputen)
else:
    print("meh?")
    
"""
thing = associations.reverse()
zipcryp = zip(associations, thing)
if Question == 'e':
    enput = print(input("Message:"))
    key = print(input("Key: "))
    print(key)
elif    Question == 'd':
    print("Message:")
elif    Question == 'q':
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
Enter e to encrypt, d to decrypt, or q to quit: z
Did not understand command, try again.
Enter e to encrypt, d to decrypt, or q to quit: e
Message: Two plus two = Five
Key: Lorem ipsum
+KF;B(CH=NIZ}m;R\Dt
Enter e to encrypt, d to decrypt, or q to quit: d
Message: +KF;B(CH=NIZ}m;R\Dt
Key: Lorem ipsum
Two plus two = Five
Enter e to encrypt, d to decrypt, or q to quit: q
Goodbye!
message =  print('Hello, do you know my other computer is your computer?')
translated =  ' '   
i = len(message)  -  1   
while  i >=  0 :   
         translated = translated + message[i]      
         i  =  i  =  1     
print(translated)
"""