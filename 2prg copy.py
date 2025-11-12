import string

plain = string.ascii_uppercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

def mono_encrypt(text):
    return text.upper().translate(str.maketrans(plain, key))

def mono_decrypt(text):
    return text.upper().translate(str.maketrans(key, plain))

text = "INFORMATION SECURITY"
enc = mono_encrypt(text)
dec = mono_decrypt(enc)

print("Plaintext: ", text)
print("Encrypted: ", enc)
print("Decrypted: ", dec)
