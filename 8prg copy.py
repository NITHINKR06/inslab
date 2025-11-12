# vigenere_cipher_compact.py
def process(text, key, decrypt=False):
    key = ''.join(c.upper() for c in key if c.isalpha()) or 'A'
    out, j = [], 0
    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            shift = ord(key[j % len(key)]) - 65
            val = (ord(ch) - ord(base) + (-shift if decrypt else shift)) % 26
            out.append(chr(val + ord(base)))
            j += 1
        else:
            out.append(ch)
    return ''.join(out)

if __name__ == "__main__":
    print("=== Vigenère Cipher ===")
    text = "INFORMATION NETWORK SECURITY"
    key = "ViGeNere-Key-123!"
    enc = process(text, key)
    dec = process(enc, key, decrypt=True)
    print("\nPlaintext :", text)
    print("Key       :", key)
    print("Encrypted :", enc)
    print("Decrypted :", dec)
