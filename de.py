from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

secret_key1 = b'secretkey'
secret_key2 = b'secretkey'

encoded_script = "2D4ILpVBdKagCehAv+jtpb1Bjb2mDfFWwI8IZY2y+XVjqkCtPmKbL9k3D/oa8MNYNE7HhjAXESNC6yFYta0RGps0m8Om94AOHtI9dgEgD8e6k7V+3FCMU2rHqkEO/zbxujznGMVS6xYf3U9a20veI1SWmiOvSGH9zuPgIm6aAuszdEghjA/Bu3mfpXprrpOl/5d273VKQfteHrYpjEK9UBHVhMXIKuDbxQoj0IdFAC4kqxIMf6o7+bB9HwyzLt0qA55YmU6d0MdRNKYThU7UBMcBKK3Gh3ryJ4ij6za9MBs3mlFRV2U8F3fD00FqEhDEwH1I6F/c5gHU8Nxl8PnO1xj7x7Hak8O51q3MX+CMMiWuB3pWmIOeeLF9pji711y/rPpbpP9VSXfAkrbyTPdzo5olAXO3wYuaar1/Pwp9pvVNcIkCemWbQX+NV2Ldx4AgBKY6jGQLTzQAQDpy69VDdSmza+5GC9opikISPPX8LdQ7jt66l7RyYWXzg3J09PTnK5S8A2ezTepDUf4Zn6/0nhKLxIHjQ9z2XrSYe+8wN3MR6dfeyFbhYSMfEj2cRbxRPCYpazkDzKcS5iq/9uhn+QsKYmfgyWu2M5KG5VLQKQwIoB4qOs8xEC4Kah+rGjPshrf65Jeeh2WWtmcobmZ05L+sO9tSUfHjcCmaDU7OSVMdk4auBG0HWXvY4lbjCDXUX5BtMbe9sPbwOj+xMl6urf4Jmup4dyQy5qlAAhfsn9g="
decoded_script = base64.b64decode(encoded_script)

iv = decoded_script[:AES.block_size]
encrypted_script = decoded_script[AES.block_size:]

cipher1 = AES.new(secret_key2, AES.MODE_CBC, iv)

decrypted_script = unpad(cipher1.decrypt(encrypted_script), AES.block_size).decode('utf-8')

#2
decoded_script2 = base64.b64decode(decrypted_script)

iv2 = decoded_script2[:AES.block_size]
encrypted_script2 = decoded_script2[AES.block_size:]

cipher2 = AES.new(secret_key1, AES.MODE_CBC, iv2)

decrypted_script2 = unpad(cipher2.decrypt(encrypted_script2), AES.block_size).decode('utf-8')

#print(decrypted_script2)
exec(decrypted_script2)
