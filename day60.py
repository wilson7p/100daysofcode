#Monoalphabetic Substitution Cipher - Vernam Cipher.
print ("\nWilson - Day 60 of #100DaysOfCode\n") 
print("\nMonoalphabetic Substitution Cipher - Vernam Cipher\n")

def vernam_cipher(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Plaintext and key must have the same length")

    ciphertext = ''
    for i in range(len(plaintext)):
        char = chr(ord(plaintext[i]) ^ ord(key[i]))
        ciphertext += char

    return ciphertext

def main():
    plaintext = "Wilson"
    key = "KJHG&*"

    if len(plaintext) != len(key):
        raise ValueError("Plaintext and key must have the same length")

    ciphertext = vernam_cipher(plaintext, key)

    print("Plaintext:", plaintext)
    print("Key:", key)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()

