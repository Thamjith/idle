from cryptography.fernet import Fernet

cipherText = input("enter the cipher text\n")
cipherText = bytes(cipherText, 'utf-8')
f = Fernet(b'N0oW_ObT2SxvI2wiwBFX0FGjvN70WfAoNIaeksl4t08=')
plainTextEncoded = f.decrypt(cipherText)
plainText = str(plainTextEncoded, 'utf-8')
print("\n" + plainText)