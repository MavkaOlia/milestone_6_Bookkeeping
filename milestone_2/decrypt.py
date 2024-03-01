# decryption function

# def decrypt(message: str, key: int):
#     res = ""
 
#     # traverse text
#     for i in range(len(message)):
#         char = message[i]
 
#         # Decrypt uppercase characters
#         if (char.isupper()):
#             res += chr((ord(char) - key-65) % 26 + 65)
 
#         # Decrypt lowercase characters
#         else:
#             res += chr((ord(char) - key - 97) % 26 + 97)
 
#     return res

# print(decrypt("Khoor", 3))

file = open("encrypt.py")