"""
cryptography.py
Author: Joe Richter
Credit: https://www.codementor.io/python/tutorial/python-encryption-message-in-python-via-reverse-cipher

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
assc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
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