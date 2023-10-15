def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

plain_text = input("Masukkan plaintext: ")
key = input("Masukkan key: ")

encrypted_text = vigenere_encrypt(plain_text, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
