import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from cryptography.fernet import Fernet
import EncryptionLogic as el

_TripleDESSelected = False
_RSA = False
_Blowfish = False
_Twofish = False
_AES = False
filename = ''
key = ''

def SelectFile():
    global filename
    global key
    key = open("key.key", "rb").read()
    filename = askopenfilename()

def TripleDESPress():
    global _TripleDESSelected
    global _RSA
    global _Blowfish
    global _Twofish
    global _AES
    _TripleDESSelected = True
    _RSA = False
    _Blowfish = False
    _Twofish = False
    _AES = False
    tripleDESButton.config(relief='sunken',bg='#08116e')
    rsaButton.config(relief='raised',bg='SystemButtonFace')
    blowfishButton.config(relief='raised',bg='SystemButtonFace')
    twoFishButton.config(relief='raised',bg='SystemButtonFace')
    aesButton.config(relief='raised',bg='SystemButtonFace')
def RSAPress():
    global _TripleDESSelected
    global _RSA
    global _Blowfish
    global _Twofish
    global _AES
    _TripleDESSelected = False
    _RSA = True
    _Blowfish = False
    _Twofish = False
    _AES = False
    tripleDESButton.config(relief='raised',bg='SystemButtonFace')
    rsaButton.config(relief='sunken',bg='#08116e')
    blowfishButton.config(relief='raised',bg='SystemButtonFace')
    twoFishButton.config(relief='raised',bg='SystemButtonFace')
    aesButton.config(relief='raised',bg='SystemButtonFace')
def BlowfishPress():
    global _TripleDESSelected
    global _RSA
    global _Blowfish
    global _Twofish
    global _AES
    _TripleDESSelected = False
    _RSA = False
    _Blowfish = True
    _Twofish = False
    _AES = False
    tripleDESButton.config(relief='raised',bg='SystemButtonFace')
    rsaButton.config(relief='raised',bg='SystemButtonFace')
    blowfishButton.config(relief='sunken',bg='#08116e')
    twoFishButton.config(relief='raised',bg='SystemButtonFace')
    aesButton.config(relief='raised',bg='SystemButtonFace')
def TwofishPress():
    global _TripleDESSelected
    global _RSA
    global _Blowfish
    global _Twofish
    global _AES
    _TripleDESSelected = False
    _RSA = False
    _Blowfish = False
    _Twofish = True
    _AES = False
    tripleDESButton.config(relief='raised',bg='SystemButtonFace')
    rsaButton.config(relief='raised',bg='SystemButtonFace')
    blowfishButton.config(relief='raised',bg='SystemButtonFace')
    twoFishButton.config(relief='sunken',bg='#08116e')
    aesButton.config(relief='raised',bg='SystemButtonFace')
def AESPress():
    global _TripleDESSelected
    global _RSA
    global _Blowfish
    global _Twofish
    global _AES
    _TripleDESSelected = False
    _RSA = False
    _Blowfish = False
    _Twofish = False
    _AES = True
    writeKeyButton.config(relief='raised',bg='SystemButtonFace')
    #rsaButton.config(relief='raised',bg='SystemButtonFace')
    #blowfishButton.config(relief='raised',bg='SystemButtonFace')
    #twoFishButton.config(relief='raised',bg='SystemButtonFace')
    aesButton.config(relief='sunken',bg='#08116e')
def EncryptButtonPress():
    global filename
    #Checks if nothing is selected
    if not _TripleDESSelected and not _RSA and not _Blowfish and not _Twofish and not _AES:
        tk.messagebox.showerror(title='Error',message='Please select an encryption method above.')
    #Checks TripleDES
    elif _TripleDESSelected and not _RSA and not _Blowfish and not _Twofish and not _AES:
        #EncryptionLogic is called for encryption
        #el.TripleDES(filename)
        print("encrypted")
        return
    #Checks RSA
    elif not _TripleDESSelected and _RSA==True and not _Blowfish and not _Twofish and not _AES:
    #EncryptionLogic is called for encryption
        print("encrypted1")
        return
    #Checks Blowfish
    elif not _TripleDESSelected and not _RSA and _Blowfish and not _Twofish and not _AES:
    #EncryptionLogic is called for encryption
        print("encrypted2")
        return
    #Checks Twofish
    elif not _TripleDESSelected and not _RSA and not _Blowfish and _Twofish and not _AES:
    #EncryptionLogic is called for encryption
        print("encrypted3")
        return
    #Checks AES
    elif not _TripleDESSelected and not _RSA and not _Blowfish and not _Twofish and _AES:
    #EncryptionLogic is called for encryption
        el.AESEncryption(filename)
        print("encrypted4")
        return
    #canvas1.create_window(500,400,window=buttonPressed)
    print("button pressed")
def DecryptButtonPress():
   # canvas1.create_window(500,400,window=el.Decrypt(filename,el.load_key))
    el.Decrypt(filename,key)
    print("button pressed")

rootWindow = tk.Tk()

rootWindow.title("Select a file")
canvas1 = tk.Canvas(rootWindow, width = 1500, height = 500)

writeKeyButton=tk.Button(canvas1,width=10,text='Gen Key',command=el.write_key)
rsaButton=tk.Button(canvas1,width=10,text='RSA',command=RSAPress)
#blowfishButton=tk.Button(canvas1,width=10,text='Blowfish',command=BlowfishPress)
#twoFishButton=tk.Button(canvas1,width=10,text='Twofish',command=TwofishPress)
aesButton=tk.Button(canvas1,width=10,text='AES',command=AESPress)

selectFileButton = tk.Button(canvas1,width=10,text='Select File',command=SelectFile)

encryptButton = tk.Button(canvas1,bg='#4fe813',activebackground='#2e8a0a',activeforeground='#1f5e06',text='Encrypt',width=10,command=EncryptButtonPress)
decryptButton = tk.Button(canvas1,bg='#f21111',activebackground='#6e0808',activeforeground='#9c0c0c',text='Decrypt',width=10,command=DecryptButtonPress)
#buttonPressed = tk.Label(canvas1,text='Button pressed!')
canvas1.pack()
canvas1.create_window(250,100,window=writeKeyButton)
#canvas1.create_window(500,100,window=rsaButton)
#canvas1.create_window(750,100,window=blowfishButton)
#canvas1.create_window(1000,100,window=twoFishButton)
canvas1.create_window(1250,100,window=aesButton)
canvas1.create_window(500,400,window=encryptButton)
canvas1.create_window(1000,400,window=decryptButton)
canvas1.create_window(750,250,window=selectFileButton)

#filename = askopenfilename()
#el.test(filename)


rootWindow.title("Encryption and Decryption")

rootWindow.mainloop()