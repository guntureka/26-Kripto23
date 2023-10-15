import numpy as np

def input_text(string):
    return input("Masukkan " + string + ": ")
    
def input_size(n):
    return int(input("Masukan size matrix: "))

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def determinant_matrix(key):
    return int(np.linalg.det(key))
    

def invers_matrix(key):
    det = determinant_matrix(key)
    det_inv = mod_inverse(det % 26, 26)
    if det_inv == -1:
        raise ValueError("Determinan matriks tidak memiliki invers modulo 26.")
  
    key = det_inv * np.round(det * np.linalg.inv(key)).astype(int) % 26
    
    return key

# matrix input
def matrix(mx):
    print(f'Masukan {mx}x{mx} dengan (spasi):')
    elements = list(map(int, input().split()))
    if len(elements) != mx * mx:
        raise ValueError(f'Expected {mx}x{mx} elements, but received {len(elements)} elements.')
    return np.array(elements).reshape(mx, mx)

# encryption code
def encrypt(plainText, key):
    n = len(key)
    plainText = plainText.replace(" ","").upper()
    encryptedText = ""
    while(len(plainText) % n != 0):
        plainText += "Z"
    for i in range(0, len(plainText), n):
        block = [ord(c) - ord('A') for c in plainText[i:i + n]]
        encryptedBlock = np.matmul(key, block) % 26
        encryptedText += "".join(chr(c + 65) for c in encryptedBlock)
    return encryptedText

# decryption code
def decrypt(cipherText, key):
    n = len(key)
    decryptedText = ""
    key_inv = invers_matrix(key)

    for i in range(0, len(cipherText), n):
        block = [ord(c) - ord('A') for c in cipherText[i:i + n]]
        decryptedBlock = np.matmul(key_inv, block) % 26
        decryptedText += "".join(chr(int(c) + 65) for c in decryptedBlock)
    return decryptedText

def find_key(plainText, cipherText,m):
    n = m
    plainText = plainText.replace(" ","").upper()
    cipherText = cipherText.replace(" ","").upper()
    key = []
    plaintTextBlock = []
    cipherTextBlock = []
    
    for i in range(n):
        rowPlainText = []
        rowCipherText = []
        for j in range(n):
            rowCipherText.append(ord(cipherText[i*n+j]) - ord('A'))
            rowPlainText.append(ord(plainText[i*n+j]) - ord('A'))
        plaintTextBlock.append(rowPlainText)
        cipherTextBlock.append(rowCipherText)
    
    plaintTextBlock = np.transpose(plaintTextBlock)
    cipherTextBlock = np.transpose(cipherTextBlock)
    inverse_matrix = invers_matrix(plaintTextBlock)

    key = np.matmul(cipherTextBlock,inverse_matrix) % 26
    
    return key
    

# main code
while True:
    print("\n=== Hill Cipher ===")
    print("1. Enkripsi\n2. Dekripsi\n3. Cari Key\n4. Keluar")
    pilihan = input("Pilihan (1/2/3/4): ")
    if pilihan == '1':
        plaintText = input_text("plaintext")
        matrix = matrix(int(input("Masukan size matrix: ")))
        encryptedText = encrypt(plaintText, matrix)
        print("\nHasil Enkripsi: ", encryptedText)
        
    if pilihan == '2':
        cipherText = input_text("ciphertext")
        matrix = matrix(int(input("Masukan size matrix: ")))
        decryptedText = decrypt(cipherText, matrix)
        print("\nHasil Dekripsi: ", decryptedText)
        
    if pilihan == '3':
        plaintText = input_text("plaintext")
        cipherText = input_text("ciphertext")
        size = input_size("size")
        key = find_key(plaintText, cipherText, size)
        print("\nHasil Key: \n", key)
        
    if pilihan == '4':
        exit()
    else:
        print("Pilihan tidak ada. Silahkan masukkan pilihan yang benar.")



        
        
    
    
    

