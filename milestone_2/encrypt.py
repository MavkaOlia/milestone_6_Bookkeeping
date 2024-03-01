# decryption function

# in VS code applying data types in arguments gives an error, 
# but in online editor it works

def encrypt(message: str, key: int):
    res = ""
 
    # traverse text
    for i in range(len(message)):
        char = message[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            res += chr((ord(char) + key-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            res += chr((ord(char) + key - 97) % 26 + 97)
 
    return res


print(encrypt("Hello", 3))