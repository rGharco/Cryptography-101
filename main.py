constSpecialCharacters = {"!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", " "}

def caesarEncryption(message="",key=0):
    encryptedMessage = ""
    for char in message:
        
        if char in constSpecialCharacters:
            encryptedMessage += char
            continue
        
        elif (ord(char.lower()) + key) > 122:
            charBeforeTransformation = ord(char.lower())
            char = ord('a') if char.lower() == char else ord('A')
            char = chr(char + (key - (122 - charBeforeTransformation)))
            
        else:
            char = chr(ord(char)+key)
        
        encryptedMessage += char
        
    return encryptedMessage

print("\n[==================================================================================]\n")

message = str(input("Enter a message: "))
key = int(input("Enter a numerical key: "))
print("\nCaesar Encryption: ", caesarEncryption(message,key))


print("\n[==================================================================================]\n")