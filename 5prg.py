def power(a, b, p):
    """Compute a^b mod p efficiently."""
    return pow(a, b, p)

# Diffie-Hellman parameters (public)
p = 353 # A large prime number
g = 3 # Primitive root modulo p
# Alice's side
a = 97 # Alice's private key
A = power(g, a, p) # Alice's public key
# Bob's side
b = 233 # Bob's private key
B = power(g, b, p) # Bob's public key
# Key exchange
# Each party uses the other's public key and their own private key
alice_shared = power(B, a, p)
bob_shared = power(A, b, p)
print("Prime number (p):", p)
print("Primitive root (g):", g)
print("Alice's private key:", a)
print("Alice's public key:", A)
print("Bob's private key:", b)
print("Bob's public key:", B)
print("Shared key calculated by Alice:", alice_shared)
print("Shared key calculated by Bob:", bob_shared)