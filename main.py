from encryption_module import encrypt_file
from decryption_module import decrypt_file

def main():
    while True:
        print("\nOptions:")
        print("1. Encrypt a File")
        print("2. Decrypt a File")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            file_path = input("Enter the path of the file to encrypt: ")
            password = input("Enter the encryption password: ")
            encrypt_file(file_path, password)
            print(f"File {file_path} encrypted successfully.")
        elif choice == '2':
            encrypted_file_path = input("Enter the path of the encrypted file: ")
            password = input("Enter the password to decrypt the file: ")
            decrypt_file(encrypted_file_path, password)
            print(f"File {encrypted_file_path} decrypted successfully.")
        elif choice == '3':
            print("---------------Bye---------------")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
