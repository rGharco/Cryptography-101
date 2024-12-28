constSpecialCharacters = {"!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", " "}

def caesarEncryption(message="",key=0):
    encryptedMessage = ""
    for i in message:
        # We want the ASCII code for the character that is why we convert to bytes first and then use indexing
        # We make all letters in lower to reduce complexity and treating two separate ranges of letters at once
        currentCharASCII = bytes(str(i).lower(), 'utf-8')
        
        if i in constSpecialCharacters:
            encryptedMessage += i
            continue
            
        # The ASCII code range for letters is A=65 and z=122, the check is so that we dont get characters like {}[]% etc
        # if the current letter + the key is bigger than 122 (e.g in the case of y + 3)
        elif (currentCharASCII[0] + key) > 122:
            if i == str(i).lower():
                i = 'a'
            else:
                i = 'A'
            i = chr(ord(i)+(key-currentCharASCII[0] % 122-1))
        else:
            i = chr(ord(i)+key)
        
        encryptedMessage += i
        
    return encryptedMessage

print("[==================================================================================]\n")

print(caesarEncryption("Z bc!",4))