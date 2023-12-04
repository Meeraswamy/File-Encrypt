from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
import os

def derive_key(password, salt):
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    return key

def decrypt_file(encrypted_file_path, password):
    with open(encrypted_file_path, 'rb') as file:
        data = file.read()

    salt = data[:16]
    iv = data[16:32]
    ciphertext = data[32:]

    key = derive_key(password, salt)
    
    cipher = AES.new(key, AES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)

    decrypted_file_path = encrypted_file_path[:-4] 
    with open(decrypted_file_path, 'wb') as file:
        file.write(plaintext)

if __name__ == "__main__":
    encrypted_file_path = input("Enter the path of the encrypted file: ")
    password = input("Enter the password to decrypt the file : ")

    decrypt_file(encrypted_file_path, password)
    print(f"File {encrypted_file_path} decrypted successfully.")
