from cryptography.fernet import Fernet
import random
import secrets
import tkinter as tk
import re
import sys
import binascii
from binascii import hexlify
from functools import partial
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

#import EncryptGUI as eg
seed = []
hex_data = ''
hexArray=[]
hexLength = 0
# key1 = []
# key2 = []
# key3 = []

def ConvertBinary(filename):
    global hex_data
    bin_data = open(filename, 'rb').read()
    hex_data = binascii.hexlify(bin_data)
    print('Hexbin Data: ')
    print(hex_data)

def Encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)
def Decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open (filename, 'wb') as file:
        file.write(decrypted_data)

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

write_key()




#THIS IS A SINGLE DES KEY
    # def SeedGen(hexArray):
    #     x=0
    #     rng = random.randint(1,255)
    #     secrets.SystemRandom(rng)
    #     seed.clear()
    #     print(seed)
    #     for x in hexArray:  
    #         rng = random.randint(1,255)
    #         rng = secrets.randbelow(rng)
    #         seed.append(rng)
    #     random.shuffle(seed)
    #     return seed

def AESEncryption(filename):
    ConvertBinary(filename)
    # write_key()

    key = load_key()

    # data = hex_data.encode()
    # f = Fernet(key)
    # encrypted = f.encrypt(data)
    Encrypt(filename,key)
    #print(encrypted)
    # hexArray[:] =hex_data
    # SeedGen(hexArray)
    # key1 = seed

    # print("key1")
    # print(key1)


