from cryptography.fernet import Fernet
from time import sleep
from tkinter import *
import ctypes
from pyperclip import copy

win = Tk()

path = __file__
path = path.replace('decrypto.py', 'key.key')
# Open the file as wb to read bytes
file = open(r"A:\decrypter and encrypter\key.key", 'rb')
key = file.read()  # The key will be type bytes
file.close()


def decryptm():
    msg = dentry.get()
    enstr = str(msg)
    enbyte = enstr.encode()
    f = Fernet(key)
    decryptedbytes = f.decrypt(enbyte)
    decrypteddecoded = decryptedbytes.decode()
    print(decrypteddecoded)
    copy(decrypteddecoded)
    ctypes.windll.user32.MessageBoxW(
        0, "message decrypted and copied to clipboard. {}".format(decrypteddecoded), "decryption sucessful", 1)


def encryptm():
    msg = eentry.get()
    en = str(msg)
    en = en.encode()
    f = Fernet(key)
    de = f.encrypt(en)
    de = de.decode()
    de = str(de)
    copy(de)
    ctypes.windll.user32.MessageBoxW(
        0, "message encryted and copied to clipboard. {}".format(msg), "encryption sucessful", 1)


llabel = Label(win, text='encrypter')
rlabel = Label(win, text='decrypter')
llabel.grid(row=0, column=0)
rlabel.grid(row=0, column=1)

eentry = Entry()
eentry.grid(row=1, column=0)
dentry = Entry()
dentry.grid(row=1, column=1)

lb = Button(win, text='encrypt', command=encryptm)
rb = Button(win, text='decrypt', command=decryptm)
lb.grid(row=2, column=0)
rb.grid(row=2, column=1)


win.mainloop()
