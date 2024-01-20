#Polyaphabetic substitution Cipher - Vignere Cipher.
print ("\nWilson - Day 61 of #100DaysOfCode\n") 
print("\nPolyaphabetic substitution Cipher - Vignere Cipher\n")

def vigenere_encrypt(plaintext, keyword):
    ciphertext = ''
    keyword = keyword.upper()
    keyword_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(keyword_repeated[i]) - ord('A')
            if plaintext[i].isupper():
                ciphertext += chr((ord(plaintext[i]) + shift - ord('A')) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(plaintext[i]) + shift - ord('a')) % 26 + ord('a'))
        else:
            ciphertext += plaintext[i]

    return ciphertext

def vigenere_decrypt(ciphertext, keyword):
    plaintext = ''
    keyword = keyword.upper()
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(keyword_repeated[i]) - ord('A')
            if ciphertext[i].isupper():
                plaintext += chr((ord(ciphertext[i]) - shift - ord('A')) % 26 + ord('A'))
            else:
                plaintext += chr((ord(ciphertext[i]) - shift - ord('a')) % 26 + ord('a'))
        else:
            plaintext += ciphertext[i]

    return plaintext

plaintext = "HelloWorld"
keyword = "KEY"
encrypted_text = vigenere_encrypt(plaintext, keyword)
decrypted_text = vigenere_decrypt(encrypted_text, keyword)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
