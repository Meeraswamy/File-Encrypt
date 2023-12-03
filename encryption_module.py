from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def derive_key(password, salt):
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    return key

def encrypt_file(file_path, password):
    salt = get_random_bytes(16)
    key = derive_key(password, salt)

    with open(file_path, 'rb') as file:
        plaintext = file.read()

    cipher = AES.new(key, AES.MODE_CFB, os.urandom(16))
    ciphertext = cipher.encrypt(plaintext)

    with open(file_path + '.enc', 'wb') as file:
        file.write(salt + cipher.iv + ciphertext)

if __name__ == "__main__":
    file_path = input("Enter the path of the file to encrypt: ")
    password = input("Enter the encryption password: ")

    encrypt_file(file_path, password)
    print(f"File {file_path} encrypted successfully.")
