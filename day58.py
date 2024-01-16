#Playfair Cipher 
print ("\nWilson - Day 58 of #100DaysOfCode\n") 
print("\nPlayfair Cipher \n")

def generate_playfair_key(key):
    key = key.replace("J", "I")
    key = "".join(sorted(set(key), key=key.index))
    playfair_matrix = [['' for _ in range(5)] for _ in range(5)]
    key_iter = iter(key + "ABCDEFGHIKLMNOPQRSTUVWXYZ")
    
    for i in range(5):
        for j in range(5):
            playfair_matrix[i][j] = next(key_iter)

    return playfair_matrix

def find_char(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt_playfair(plain_text, key):
    matrix = generate_playfair_key(key)
    encrypted_text = ""
    
    def process_pair(pair):
        row1, col1 = find_char(matrix, pair[0])
        row2, col2 = find_char(matrix, pair[1])
        
        if row1 == row2:
            return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            return matrix[row1][col2] + matrix[row2][col1]

    plain_text = plain_text.replace("J", "I")
    plain_text = [plain_text[i:i+2] for i in range(0, len(plain_text), 2)]

    for pair in plain_text:
        encrypted_text += process_pair(pair)

    return encrypted_text

def main():
    key = "KEYWORD"
    plaintext = "HELLO"
    
    encrypted_text = encrypt_playfair(plaintext, key)
    
    print(f"Key: {key}")
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted Text: {encrypted_text}")

if __name__ == "__main__":
    main()

