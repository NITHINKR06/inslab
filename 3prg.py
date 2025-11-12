def generate_key_matrix(key):
    key = key.upper().replace("J", "I") # Replace J with I
    result = ""
    for c in key:
        if c.isalpha() and c not in result:
            result += c
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ": # (J is skipped)
        if c not in result:
            result += c
        # build 5x5 matrix from result
        matrix = [list(result[i*5:(i+1)*5]) for i in range(5)]
    return matrix

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    raise ValueError(f"Character {char} not found in key matrix")

def process_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join(c for c in text if c.isalpha())
    i = 0
    result = ""
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
# insert X between identical letters in a digraph
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2
# pad if odd length
    if len(result) % 2 != 0:
        result += 'X'
    return result
def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
# when on same row -> take right neighbor
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
# when on same column -> take below neighbor
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
# rectangle rule
    else:
        return matrix[row1][col2] + matrix[row2][col1]
def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    prepared = process_text(plaintext)
    ciphertext = ""
    for i in range(0, len(prepared), 2):
        ciphertext += encrypt_pair(matrix, prepared[i], prepared[i + 1])
    return ciphertext

if __name__ == "__main__":
    key = 'MONARCHY'
    plaintext = 'INSTRUMENTS'
    ciphertext = playfair_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)