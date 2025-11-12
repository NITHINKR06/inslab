import string
plain_alphabet = string.ascii_uppercase
cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM" # This acts as the key
# Encryption function

def monoalphabetic_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ''
    for char in plaintext:
        if char in plain_alphabet:
            idx = plain_alphabet.index(char)
            ciphertext += key[idx]
        else:
            ciphertext += char # Non-alphabetic characters unchanged
    return ciphertext

# Decryption function

def monoalphabetic_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    plaintext = ''
    for char in ciphertext:
        if char in key:
            idx = key.index(char)
            plaintext += plain_alphabet[idx]
        else:
            plaintext += char
    return plaintext

text = "INFORMATION SECURITY" # Example with space (will be left unchanged)
key = cipher_alphabet
encrypted = monoalphabetic_encrypt(text, key)
decrypted = monoalphabetic_decrypt(encrypted, key)
print("Plaintext: ", text)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)