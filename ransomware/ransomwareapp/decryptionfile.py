from cryptography.fernet import Fernet
import os
from ransomwareapp.models import AttackData

changed_file_list=[]
def decryption(decrypt_key,directory_path,Org_file_list):

   
    i=0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if 'lazarus' in file.split('.'):
                file_path = os.path.join(root, file)
                changed_file_list.append(file_path)
    
    print(changed_file_list)
    for changed_file in changed_file_list:

        if i<=len(changed_file_list):
            with open(changed_file, 'rb') as file:
                changed_data = file.read()
            key = decrypt_key
            fernet = Fernet(key)
            decrypted = fernet.decrypt(changed_data)

            with open(changed_file, 'wb') as decrypted_file:
                
                decrypted_filename = Org_file_list[i]
                # print(file)
                decrypted_file.write(decrypted)
                os.rename(changed_file,decrypted_filename)
        
        i+=1
    AttackData.objects.all().delete()
