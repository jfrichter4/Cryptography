"""
cryptography.py
Author: Joe Richter
Credit: https://www.codementor.io/python/tutorial/python-encryption-message-in-python-via-reverse-cipher

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
Question = print(input("Enter e to encrypt, d to decrypt, or q to quit: "))
if Question == 'e':
    print(...)
    elif Question == 'd':
        print(...)
    elif Question == 'q':
        print("Goodbye!")
    else print(Two plus two = Five)
    
    
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
message =  ‘Hello, do you know my other computer is your computer?’ 
translated =  ‘ ‘   
i = len(message)  -  1   
while  i >=  0 :   
         translated = translated + message[i]      
         i  =  i  =  1     
print(translated)