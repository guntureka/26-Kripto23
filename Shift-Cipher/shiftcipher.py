

def encrypt(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            
            char_code = ord(char)
            char_code = (char_code - 97 + shift) % 26 + 97
            
            char = chr(char_code)
            if is_upper:
                char = char.upper()
                
        result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

text = input("Enter text: ")
shift = int(input("Enter Shift: "))
encrypted_text = encrypt(text, shift)
decrypt_text = decrypt(encrypted_text, shift)

print("Plaintext: ", text)
print("Encrypted: ", encrypted_text)
print("Decrypted: ", decrypt_text)


    
    