# vigenere_cipher.py
import string

ALPHA = string.ascii_uppercase

def normalize_key(key: str) -> str:
    """Return uppercase-only letter key; raise if no letters."""
    k = ''.join([c.upper() for c in key if c.isalpha()])
    if not k:
        raise ValueError("Key must contain at least one letter (A-Z).")
    return k

def vigenere_encrypt(plaintext: str, key: str) -> str:
    key = normalize_key(key)
    key_len = len(key)
    result = []
    ki = 0
    for ch in plaintext:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            p = ord(ch) - ord(base)
            k = ord(key[ki % key_len]) - ord('A')
            c = (p + k) % 26
            result.append(chr(c + ord(base)))
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    key = normalize_key(key)
    key_len = len(key)
    result = []
    ki = 0
    for ch in ciphertext:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            c = ord(ch) - ord(base)
            k = ord(key[ki % key_len]) - ord('A')
            p = (c - k + 26) % 26
            result.append(chr(p + ord(base)))
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    print("=== Vigenère Cipher ===")
    text = ' INFORMATION NETWORK SECURITY'
    key = 'ViGeNere-Key-123!'

    try:
        enc = vigenere_encrypt(text, key)
        dec = vigenere_decrypt(enc, key)
        print("\nPlaintext :", text)
        print("Key       :", key)
        print("Encrypted :", enc)
        print("Decrypted :", dec)
    except ValueError as e:
        print("Error:", e)
