'''import sys
from collections import Counter

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryptedMessage = "Zdrxzerkzfe zj dfiv zdgfikrek kyre Befncvuxv"

def frequencyAttack(cipherText):
    cipherText = cipherText.upper()
    #{letter, frequency}
    letter_freq = {}
    #initial values of each letter is 0
    for letter in ALPHABET:
        letter_freq[letter] = 0
    for letter in cipherText:
        if letter in ALPHABET:
            letter_freq[letter] += 1
    return letter_freq


def freq(cipherInput):
    # stripping whitespace
    noWhiteSpaceText = cipherInput.replace(" ", "")
    freqText = ""
    # capitalize all non-white space frequency attack text
    for letter in noWhiteSpaceText:
        if letter == " ":
            freqText += letter
        else:
            freqText += letter.upper()

    #frequency dictionary
    counts = Counter(freqText)
    return counts

#returns the key that has the max value from the dictionary
def keyMaxVal(d):
    v = list(d.values())
    k = list(d.keys())
    #v=[5,4,4,3,5], k=["Z","D","F"]

    return k[v.index(max(v))]

def main():

    exitCode = "n"
    decryptedMessage = ""
    encMessage = input("Enter ciphertext: ")
    #a dictionary of letters and their frequency
    freqDict = freq(encMessage)
    #key with the maximum value in the dictionary
    keyMax = keyMaxVal(freqDict)
    #find the index of the max key
    maxKeyIndex = ALPHABET.find(keyMax)
    decryptedIndex = (maxKeyIndex - maxKeyIndex) % 26
    print("One of the most frequent letter besides E(most common letter in English) is", keyMax,
          ", decrypted is", ALPHABET[decryptedIndex], )
    print("Using", maxKeyIndex,"as the shift key")

    #2nd attempt using dynamic frequency attacks

    letterFreq = frequencyAttack(encMessage) #returns a dict with {key = A-Z: value = any integer}
    #store used encryption key's value
    usedEncryptionKey = []
    upperEncryptionMessage = encMessage.upper()

    print(upperEncryptionMessage)
    decMsg = ""
    freq_items = letterFreq.items()
    for k, v in freq_items:
        if k not in usedEncryptionKey:
            mostFrequentLetter = keyMaxVal(freq_items)
            for letter in upperEncryptionMessage:
                # if space, then ignore;
                if letter == " ":
                    decMsg += letter
                else:
                    index = ALPHABET.find(mostFrequentLetter)
                    decIndex = (index - maxKeyIndex) % 26
                    decMsg += ALPHABET[decIndex]
            print("Is it ", decMsg, " ?")
            answer = input("y or n: ")
            if answer == "n":
                print(
                    "Continuing with half range...")  # could have found the next frequent letter index but not enough time
            else:
                sys.exit()

            #usedEncryptionKey.append(mostFrequentLetter)













    upperCaseEncMessage = ""

    for letter in encMessage:
        if letter == " ":
            upperCaseEncMessage += letter
        else:
            upperCaseEncMessage += letter.upper()

    #decrypt with frequency analysis
    upperCaseEncMessage1 = upperCaseEncMessage
    decryptedMessage1 = ""
    for letter in upperCaseEncMessage1:
        #if space, then ignore;
        if letter == " ":
            decryptedMessage1 += letter
        else:
            index = ALPHABET.find(letter)
            decIndex = (index - maxKeyIndex) % 26
            decryptedMessage1 += ALPHABET[decIndex]
    print("Is it ", decryptedMessage1, " ?")
    answer = input("y or n: ")
    if answer == "n":
        print("Continuing with half range...") # could have found the next frequent letter index but not enough time
    else:
        sys.exit()

        #brute force range(13-26)
    for key in range(13, 26):
        for letter in upperCaseEncMessage:
            if letter == " ":
                decryptedMessage += letter
            else:
                index = ALPHABET.find(letter)
                decIndex = (index - key) % 26
                decryptedMessage += ALPHABET[decIndex]
        print("Is it ", decryptedMessage, " ?")
        answer = input("y or n: ")
        if answer == "n":
            decryptedMessage = ""
            continue
        else:
            sys.exit()

    #brute force range(0,13)
    for key in range(0, 13):
        for letter in upperCaseEncMessage:
            if letter == " ":
                decryptedMessage += letter
            else:
                index = ALPHABET.find(letter)
                decIndex = (index - key) % 26
                decryptedMessage += ALPHABET[decIndex]
        print("Is it ", decryptedMessage, " ?")
        answer = input("y or n: ")
        if answer == "n":
            decryptedMessage = ""
            continue
        else:
            sys.exit()

if __name__ == '__main__':
    main()


'''

