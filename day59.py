#Monoalphabetic Substitution Cipher - Affine Cipher.
print ("\nWilson - Day 59 of #100DaysOfCode\n") 
print("\nMonoalphabetic Substitution Cipher - Affine Cipher\n")

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(plain_text, a, b):
    result = ""
    m = 26
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                result += chr((a * (ord(char) - ord('A')) + b) % m + ord('A'))
            else:
                result += chr((a * (ord(char) - ord('a')) + b) % m + ord('a'))
        else:
            result += char
    return result

def affine_decrypt(cipher_text, a, b):
    result = ""
    m = 26
    a_inv = mod_inverse(a, m)
    if a_inv is not None:
        for char in cipher_text:
            if char.isalpha():
                if char.isupper():
                    result += chr((a_inv * (ord(char) - ord('A') - b)) % m + ord('A'))
                else:
                    result += chr((a_inv * (ord(char) - ord('a') - b)) % m + ord('a'))
            else:
                result += char
        return result
    else:
        return "Invalid key: 'a' must be coprime with the alphabet size."

plain_text = "Hello, World!"
a = 5
b = 8

cipher_text = affine_encrypt(plain_text, a, b)
print("Encrypted:", cipher_text)

decrypted_text = affine_decrypt(cipher_text, a, b)
print("Decrypted:", decrypted_text)
