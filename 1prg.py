# caesar_cipher.py
def caesar_encrypt(plaintext: str, key: int) -> str:
    ciphertext = []
    key = key % 26
    for ch in plaintext:
        if 'A' <= ch <= 'Z':
            ciphertext.append(chr((ord(ch) - ord('A') + key) % 26 + ord('A')))
        elif 'a' <= ch <= 'z':
            ciphertext.append(chr((ord(ch) - ord('a') + key) % 26 + ord('a')))
        else:
            ciphertext.append(ch)
    return ''.join(ciphertext)

def caesar_decrypt(ciphertext: str, key: int) -> str:
    return caesar_encrypt(ciphertext, -key)

if __name__ == "__main__":
    print("=== Caesar Cipher ===")
    text = input("Enter text: ")
    while True:
        try:
            key = int(input("Enter key (integer, e.g. 1-25): "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    encrypted = caesar_encrypt(text, key)
    decrypted = caesar_decrypt(encrypted, key)
    print("\nEncrypted text:", encrypted)
    print("Decrypted text:", decrypted)
