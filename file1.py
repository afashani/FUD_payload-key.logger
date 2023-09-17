from cryptography.fernet import Fernet

encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)

input_file = 'de.py'
output_file = 'de_out.txt'

with open(input_file, 'rb') as file:
    plaintext = file.read()

ciphertext = cipher.encrypt(plaintext)

with open(output_file, 'wb') as file:
    file.write(ciphertext)

print("Encryption key:", encryption_key)
