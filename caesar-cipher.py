def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet  + alphabet
    return doubleAlphabet
alphabet="ABC"


def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input("Please enter a key(whole number from 1-25): ")
    return shiftAmount

#encrypting message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage =""
    upperCaseMessage =""
    upperCaseMessage = message.upper()
    for currentCharacter in upperCaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

#decrypting message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

#main function
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()