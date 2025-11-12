# Short RSA Encryption and Decryption (same output as full version)

p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = pow(e, -1, phi)  # modular inverse of e mod phi

print("Public key :", (e, n))
print("Private key:", (d, n))

plaintext = "HELLO"
plain_nums = [ord(c) - 65 for c in plaintext]
print("Plain numbers:", plain_nums)

cipher_nums = [pow(m, e, n) for m in plain_nums]
print("Encrypted numbers:", cipher_nums)

decrypted_nums = [pow(c, d, n) for c in cipher_nums]
decrypted_text = ''.join(chr(m + 65) for m in decrypted_nums)
print("Decrypted text:", decrypted_text)
