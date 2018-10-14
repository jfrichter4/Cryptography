"""
cryptography.py
Author: Joe Richter
Credit: https://www.codementor.io/python/tutorial/python-encryption-message-in-python-via-reverse-cipher

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
assc =  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]- = _+?!"
Straight = {}
Reverse = {}
while True:
    Question = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if Question == 'q':
        print("Goodbye!")
        break
    elif Question == 'e':
        mESSAGE= input("Message: ")
        kEY = input("Key: ")
        mESSAGElist = []
        kEYlist = []
        for q in mESSAGE:
            mESSAGElist.append(assc.find(q))
        for w in kEY:
            kEYlist.append(assc.find(w))
        times = len(mESSAGElist)/len(kEYlist)+1
        kEYlist = int(times)*kEYlist
        encryption = []
        for e in range(0,len(mESSAGElist)):
            encryption.append(mESSAGElist[e]+kEYlist[e])
        new = []
        count = (len(assc))
        for r in encryption:
            if r >= (count-1):
                multiple = r//count+1
                num = r-multiple*count
                new.append(assc[num])
            else:
                new.append(assc[r])
        new = "".join(new)
        print(new)
    elif Question == 'd':
        mESSAGE= input("Message: ")
        kEY = input("Key: ")
        mESSAGElist = []
        kEYlist = []
        for t in mESSAGE:
            mESSAGElist.append(assc.find(t))
        for y in kEY:
            kEYlist.append(assc.find(y))
        times = len(mESSAGElist)/len(kEYlist)+1
        kEYlist = int(times)*kEYlist
        decryption = []
        for u in range(0,len(mESSAGElist)):
            decryption.append(mESSAGElist[u]-kEYlist[u])
        new = []
        count = (len(assc))
        for i in decryption:
            if i<0:
                num = (count)+i
                new.append(assc[num])
            else:
                new.append(assc[i])
        new = "".join(new)
        print(new)
    else:
        print("Did not understand command, try again.")
        continue

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
            print(outputen)
else:
    print("meh?")
    

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

import cryptography
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)
import cryptography
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)
btw: https://docs.python-guide.org/scenarios/crypto/
"""