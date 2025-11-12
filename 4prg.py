# Short 2x2 Hill cipher (exam-friendly)
import re
M = 26 # modulus for A..Z
def clean(s):
    """Uppercase letters only, pad with X if odd length."""
    s = re.sub(r'[^A-Za-z]', '', s).upper()
    if len(s) % 2 == 1:
        s += 'X'
    return s

def c2n(c): return ord(c) - ord('A') # A->0, B->1, ...

def n2c(n): return chr((n % M) + ord('A')) # 0->A, 1->B, ...

def egcd(a, b):
    if b == 0: return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modinv(a, m=M):
    a %= m
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No inverse (key not invertible)")
    return x % m
# 2x2 matrix ops

def matmul2(K, vec):
    (a,b),(c,d) = K
    x,y = vec
    return ((a*x + b*y) % M, (c*x + d*y) % M)

def matinv2(K):
    (a,b),(c,d) = K
    det = (a*d - b*c) % M
    inv_det = modinv(det)
# adjugate [[d, -b], [-c, a]]
    return (( (inv_det * d) % M, (inv_det * (-b)) % M ),
( (inv_det * (-c)) % M, (inv_det * a) % M ))

# encrypt / decrypt
def encrypt(pt, K):
    p = clean(pt)
    out = []
    for i in range(0, len(p), 2):
        x, y = c2n(p[i]), c2n(p[i+1])
        u, v = matmul2(K, (x, y))
        out.append(n2c(u) + n2c(v))
    return ''.join(out)

def decrypt(ct, K):
    c = clean(ct)
    Kinv = matinv2(K)
    out = []
    for i in range(0, len(c), 2):
        x, y = c2n(c[i]), c2n(c[i+1])
        u, v = matmul2(Kinv, (x, y))
        out.append(n2c(u) + n2c(v))
    return ''.join(out)

# Example
if __name__ == '__main__':
    K = ((3,3),(2,5))
    pt = "HELLO WORLD"
    ct = encrypt(pt, K)
    rt = decrypt(ct, K)
    print("Plain:", pt)
    print("Cipher:", ct)
    print("Recovered:", rt)