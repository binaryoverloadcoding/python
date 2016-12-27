#Challenge 19 - William Oldham

def encrypt(text, key):
    newString = ""
    for letter in text:
        originalAscii = ord(letter)
        newAscii = originalAscii + key
        newString = newString + chr(newAscii)
    return newString

def decrypt(text, key):
    newString = ""
    for letter in text:
        originalAscii = ord(letter)
        newAscii = originalAscii - key
        newString = newString + chr(newAscii)
    return newString

text = input("Enter text to encrypt/decrypt: ")
key = int(input("Enter key to encrypt/decrypt: "))
what = input("Encrypt or Decrypt[E/D]: ")

if what.lower() == "e":
    print(encrypt(text, key))
elif what.lower() == "d":
    print(decrypt(text, key))