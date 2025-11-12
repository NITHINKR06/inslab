# triple_des_toy_compact.py
import base64

def xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

plain_text = "INFORMATION NETWORK SECURITY"
k1, k2, k3 = "KEY number ONE", "KEY number TWO", "KEY number THREE"

# encrypt: E_k3(E_k2(E_k1(plaintext)))
cipher_b64 = base64.b64encode(xor(xor(xor(plain_text.encode(), k1.encode()), k2.encode()), k3.encode())).decode()

# decrypt: D_k1(D_k2(D_k3(ciphertext)))
decrypted = xor(xor(xor(base64.b64decode(cipher_b64), k3.encode()), k2.encode()), k1.encode()).decode(errors="replace")

print("=== Triple-DES style (toy) ===")
print("\nPlaintext  :", plain_text)
print("Ciphertext (base64):", cipher_b64)
print("Decrypted  :", decrypted)
print("==============================")