# triple_des_toy.py
import base64

def xor_bytes(data: bytes, key: bytes) -> bytes:
    """XOR data with key repeated."""
    out = bytearray(len(data))
    key_len = len(key)
    for i, b in enumerate(data):
        out[i] = b ^ key[i % key_len]
    return bytes(out)

def triple_des_encrypt(plain_text: str, key1: str, key2: str, key3: str) -> str:
    """
    Toy triple-DES: E_k3(E_k2(E_k1(plaintext_bytes)))
    Returns base64-encoded ciphertext string.
    NOTE: This is a teaching/demo implementation, not real 3DES.
    """
    p_bytes = plain_text.encode('utf-8')
    step1 = xor_bytes(p_bytes, key1.encode('utf-8'))
    step2 = xor_bytes(step1, key2.encode('utf-8'))
    step3 = xor_bytes(step2, key3.encode('utf-8'))
    return base64.b64encode(step3).decode('ascii')

def triple_des_decrypt(cipher_b64: str, key1: str, key2: str, key3: str) -> str:
    step3 = base64.b64decode(cipher_b64)
    step2 = xor_bytes(step3, key3.encode('utf-8'))
    step1 = xor_bytes(step2, key2.encode('utf-8'))
    p_bytes = xor_bytes(step1, key1.encode('utf-8'))
    return p_bytes.decode('utf-8', errors='replace')

if __name__ == "__main__":
    print("=== Triple-DES style (toy) ===")
    plain_text = "INFORMATION NETWORK SECURITY"
    k1 = "KEY number ONE"
    k2 = "KEY number TWO"
    k3 = "KEY number THREE"


    if not (k1 and k2 and k3):
        print("All three keys are required.")
    else:
        cipher = triple_des_encrypt(plain_text, k1, k2, k3)
        decrypted = triple_des_decrypt(cipher, k1, k2, k3)

        print("\nPlaintext  :", plain_text)
        print("Ciphertext (base64):", cipher)
        print("Decrypted  :", decrypted)
