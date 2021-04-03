def group_info():
  return [("1019790", "Ayub Saghouani", "INF1D")]



def encrypt_caesar(plaintext, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    shiftedAlphabet = alphabet[shift-26:]+ alphabet[0:(shift-26)]
    shiftedAlphabet = alphabet[shift%26:]+ alphabet[0:shift%26]
    for i in range(len(plaintext)):
        letter = plaintext[i]
        idx = alphabet.find(letter.upper())
        if idx == -1:
            ciphertext +=  letter
        elif letter.islower():
            ciphertext += shiftedAlphabet[idx].lower()
        else:
            ciphertext += shiftedAlphabet[idx] 
    return(ciphertext)


def decrypt_caesar(ciphertext, shift):
    plaintext = ''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NewShiftedAlphabet = alphabet[-shift-26:]+ alphabet[0:(-shift-26)]
    NewShiftedAlphabet = alphabet[-shift%26:]+ alphabet[0:-shift%26]
    for s in range(len(ciphertext)):
        newletter = ciphertext[s]
        index = alphabet.find(newletter.upper())
        if index == -1:
            plaintext +=  newletter
        elif newletter.islower():
            plaintext += NewShiftedAlphabet[index].lower()
        else:
            plaintext += NewShiftedAlphabet[index] 
    return(plaintext)



    
    
    
    
