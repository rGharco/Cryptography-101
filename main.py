def caesarEncryption(message="",key=0):
    encryptedMessage = ""
    for i in message:
        currentCharBinary = bytes(str(i).lower(), 'utf-8')
        if i == " ":
            encryptedMessage += i
        elif (currentCharBinary[0] + key) > 122:
            indexDifference = 122 - currentCharBinary[0]
            if i == str(i).lower():
                i = 'a'
            else:
                i = 'A'
            i = chr(ord(i)+(3-indexDifference-1))
        else:
            i = chr(ord(i)+key)
        
        encryptedMessage += i
        
    return print(f"The encrypted message is:{encryptedMessage}")

print("[==================================================================================]\n")

message = input("Enter your message: ")
key = int(input("Enter key value (int): "))
print("\nEncryption Algorithms: \n1. Caesar 2.Unknown 3.Unknown")
choice = int(input("\nEnter what encryption algorithm to use (1-3): \n"))

encryptionAlgorithms = {
    1: caesarEncryption(message,key),
    2: "Unknown",
    3: "Unknown",
}
encryptionAlgorithms.get(choice)

print("\n[==================================================================================]")