from os.path import exists
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from cryptography.fernet import Fernet


class Logic():
    filename = ''

    def file_select(self):
        global filename
        filename = askopenfilename()
        print(filename)
    
    def load_key(self):

        if exists("key.key"):
            key_to_load = open("key.key", "rb").read()
            #key_to_load.close()
        else:
            messagebox.showwarning("Key Not Found", "A new key will be generated.")
            key_to_load = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(key_to_load)
                self.load_key()
        return key_to_load

    def encrypt(self):
        key = self.load_key()
        key = Fernet(key)

        with open(filename, 'rb') as file:
            file_data = file.read()

        encrypted_data = key.encrypt(file_data)
        
        with open(filename,'wb') as file:
            file.write(encrypted_data)

    def decrypt(self):
        key = self.load_key()
        key = Fernet(key)

        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = key.decrypt(encrypted_data)
        with open(filename, 'wb') as file:
            file.write(decrypted_data)
