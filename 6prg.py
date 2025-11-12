def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Step 2: Function to find modular inverse (used for private key)
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Step 3: Choose two prime numbers
p = 61
q = 53
# Step 4: Compute n and φ(n)
n = p * q # n is the modulus for both keys
phi = (p - 1) * (q - 1) # Euler's totient function
# Step 5: Choose e (public key exponent)
e = 17 # e must be coprime with phi
# Step 6: Compute d (private key exponent)
d = mod_inverse(e, phi)
print("Public key :", (e, n))
print("Private key:", (d, n))
# Step 7: Message to encrypt
plaintext = "HELLO"
# Step 8: Convert letters to numbers (A=0, B=1, ..., Z=25)
plain_nums = [ord(c) - 65 for c in plaintext]
print("Plain numbers:", plain_nums)
# Step 9: Encrypt → c = (m^e) mod n
cipher_nums = [pow(m, e, n) for m in plain_nums]
print("Encrypted numbers:", cipher_nums)
# Step 10: Decrypt → m = (c^d) mod n
decrypted_nums = [pow(c, d, n) for c in cipher_nums]
# Step 11: Convert numbers back to letters
decrypted_text = ''.join(chr(m + 65) for m in decrypted_nums)
print("Decrypted text:", decrypted_text)