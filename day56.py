#Implementation of Ceasar Cipher 
print ("\nWilson - Day 56 of #100DaysOfCode\n") 
print("\nImplementation of Ceasar Cipher\n")

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char
    return result

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

plaintext = "wilson"
shift_value = 3
encrypted_text = caesar_cipher_encrypt(plaintext, shift_value)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_value)
print(plaintext)
print("Enc", encrypted_text)
print("Dec:", decrypted_text)
