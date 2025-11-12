# To implement Caesar Cipher encryption and decryption

def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - shift + key) % 26 + shift)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            plaintext += chr((ord(char) - shift - key) % 26 + shift)
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    print("CAESAR CIPHER Encryption and Decryption")
    text = input("Enter text: ")
    key = int(input("Enter key (1-25): "))

    encrypted = caesar_encrypt(text, key)
    decrypted = caesar_decrypt(encrypted, key)

    print("\nEncrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
