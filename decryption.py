# importing module
import os
from cryptography.fernet import Fernet
encryption_key = "./key.key"
with open(encryption_key, 'rb') as enc_key:
    de = enc_key.read()

fernet = Fernet(de)

root_folder = "./test-folder"

object = os.scandir(root_folder)

for entry in object:
    with open(entry, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

decrypted = fernet.decrypt(encrypted)


with open(entry, 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

print(f"Files are Decrypted in folder {root_folder}")

obj = os.scandir(root_folder)
for entry in obj:
    if entry.is_file():
        print(entry.name)
