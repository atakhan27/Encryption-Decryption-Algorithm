def encrypt(character,keynumber):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    for loc in range(0, len(alphabet),1):
        if character == alphabet[loc]:
            newloc = loc + keynumber
            while newloc >= 26:
                newloc -= 26
            newchar = alphabet[newloc]
            return newchar
    for loc in range(0, len(caps),1):
        if character == caps[loc]:
            newloc = loc + keynumber
            while newloc >= 26:
                newloc -= 26
            newchar = caps[newloc]
            return newchar
    for loc in range(0,len(digits),1):
        if character == digits[loc]:
            newloc = loc + keynumber
            while newloc >= 10:
                newloc -= 10
            newchar = digits[newloc]
            return newchar
    return character
def decrypt(char,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    for loc in range(0, len(alphabet),1):
        if char == alphabet[loc]:
            newloc = loc - key
            while newloc < 0:
                newloc += 26
            newchar = alphabet[newloc]
            return newchar
    for loc in range(0, len(caps),1):
        if char == caps[loc]:
            newloc = loc - key
            while newloc < 0:
                newloc += 26
            newchar = caps[newloc]
            return newchar    
    for loc in range(0,len(digits),1):
        if char == digits[loc]:
            newloc = loc - key
            while newloc < 0:
                newloc += 10
            newchar = digits[newloc]
            return newchar
    return character
# MAIN PROGRAM TO ENCRYPT / DECRYPT
finished = False
while not finished:
    encr_decr = input("Please type E if u want 2 Encrypt or type D if u want 2 Decrypt = ")
    if encr_decr != "E" and encr_decr != "D":
        finished = True
        break
    key = input("What is the encryption KEY = ")
    keyno = int(key)
    keyno = abs(key)
    if encr_decr == "E":
        message = input("What is the MESSAGE u want 2 encrypt = ")
        encryptm = ""
        for ndex in range(0,len(message),1):
            char = message[ndex]
            character = str(char)
            newchar = encrypt(char,keyno)
            encryptm = encryptm + newchar
        print("The ENCRYPRED Message is =", encryptm)
    else:
        message = input("What is the ENCRYPTED Message u want 2 decrypt = ")
        decryptm = ""
        for ndex in range(0,len(message),1):
            char = message[ndex]
            character = str(char)
            newchar = decrypt(char,keyno)
            decryptm = decryptm + newchar
        print("The DECRYPTED Message is =", decryptm)
print("MISSION ACCOMPLISHED")
