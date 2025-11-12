# monoalphabetic_cipher.py
import string

PLAIN_ALPHABET = string.ascii_uppercase

def validate_key(key: str) -> str:
    key = ''.join([c for c in key.upper() if c.isalpha()])
    if len(key) != 26 or len(set(key)) != 26:
        raise ValueError("Key must be 26 unique letters (A-Z).")
    return key

def monoalphabetic_encrypt(plaintext: str, key: str) -> str:
    key = validate_key(key)
    mapping = {p: k for p, k in zip(PLAIN_ALPHABET, key)}
    ciphertext = []
    for ch in plaintext:
        if ch.isalpha():
            up = ch.isupper()
            mapped = mapping[ch.upper()]
            ciphertext.append(mapped if up else mapped.lower())
        else:
            ciphertext.append(ch)
    return ''.join(ciphertext)

def monoalphabetic_decrypt(ciphertext: str, key: str) -> str:
    key = validate_key(key)
    inv_mapping = {k: p for p, k in zip(PLAIN_ALPHABET, key)}
    plaintext = []
    for ch in ciphertext:
        if ch.isalpha():
            up = ch.isupper()
            mapped = inv_mapping[ch.upper()]
            plaintext.append(mapped if up else mapped.lower())
        else:
            plaintext.append(ch)
    return ''.join(plaintext)

if __name__ == "__main__":
    default_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    print("=== Monoalphabetic Substitution Cipher ===")
    text = input("Enter text: ")
    key_input = input(f"Enter 26-letter key (leave blank to use default '{default_key}'): ").strip()
    key = key_input if key_input else default_key
    try:
        enc = monoalphabetic_encrypt(text, key)
        dec = monoalphabetic_decrypt(enc, key)
        print("\nPlaintext:", text)
        print("Key      :", key.upper())
        print("Encrypted:", enc)
        print("Decrypted:", dec)
    except ValueError as e:
        print("Error:", e)
