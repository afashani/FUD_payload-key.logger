from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

secret_key = b'secretkey'

with open('encrypted_script.txt', 'r') as file:
    obfuscated_script = file.read()

iv = get_random_bytes(AES.block_size)

cipher = AES.new(secret_key, AES.MODE_CBC, iv)

padded_script = pad(obfuscated_script.encode(), AES.block_size)

encrypted_script = cipher.encrypt(padded_script)

iv_and_encrypted_script = iv + encrypted_script

encoded_script = base64.b64encode(iv_and_encrypted_script)

with open('2encrypted_script.txt', 'w', encoding='utf-8') as file:
    file.write(encoded_script.decode('utf-8'))
