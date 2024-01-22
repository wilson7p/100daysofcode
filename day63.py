#Transposition Cipher - Columnar cipher.
print ("\nWilson - Day 63 of #100DaysOfCode\n") 
print("\nTransposition Cipher - Columnar cipher\n")

def encrypt(text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    encrypted_text = [text[i::len(key)] for i in key_order]
    return ''.join(encrypted_text)

def decrypt(text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    rows = len(text) // len(key) + (1 if len(text) % len(key) > 0 else 0)
    decrypted_text = [text[i * rows:(i + 1) * rows] for i in key_order]
    return ''.join(decrypted_text)

plaintext = "HELLOCOLUMNARTRANSPOSITION"
key = "COLUMNAR"

key_order = sorted(range(len(key)), key=lambda k: key[k])
encrypted_text = [plaintext[i::len(key)] for i in key_order]
encrypted_text = ''.join(encrypted_text)
print("Encrypted:", encrypted_text)

rows = len(encrypted_text) // len(key) + (1 if len(encrypted_text) % len(key) > 0 else 0)
decrypted_text = [encrypted_text[i * rows:(i + 1) * rows] for i in key_order]
decrypted_text = ''.join(decrypted_text)
print("Decrypted:", decrypted_text)
