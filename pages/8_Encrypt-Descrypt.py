from pydoc import plain
from tkinter import *

class Caesar : #deklarasi class

    def __init__(self, plainText, key):
        self.plainText = str.lower(plainText)
        self.key = key

    def encrypt(self):
        abjad = "abcdefghijklmnopqrstuvwxyz 0123456789"
        cipherText = ""
        for words in self.plainText:
            wordsIndex = (abjad.find(words)+self.key)%len(abjad)
            cipherText = cipherText+abjad[wordsIndex]
        return cipherText

    def decrypt(self):
        abjad = "abcdefghijklmnopqrstuvwxyz 0123456789"
        cipherText = ""
        for words in self.plainText:
            wordsIndex = (abjad.find(words)-self.key)%len(abjad)
            cipherText = cipherText+abjad[wordsIndex]
        return cipherText

app = Tk()
app.title("Encrypt Message")

TitleLabel = Label(app, text = "Hide Your Messages!", font = ('bold', 14))
TitleLabel.place(x=270, y=20)

plainLabel = Label(app, text = "Your text?").place(x=10, y=60)
plain = Entry(app, width=70, borderwidth=1)
plain.place(x=90, y=60)
keyCodeLabel = Label(app, text = "Key").place(x=10, y=100)
keyCode = Entry(app, width=40, borderwidth=1)
keyCode.place(x=90, y=100)
hasil = Entry(app, width=40, borderwidth=1)
hasil.place(x=90, y=140)

def ProcessEncrypt(text, key):
    cipher = Caesar(text, key)
    return cipher.encrypt()

def ProcessDecrypt(text, key):
    cipher = Caesar(text, key)
    return cipher.decrypt()

def EncryptButton():
    text = plain.get()
    key = int(keyCode.get())
    cipher = ProcessEncrypt(text, key)
    hasil.delete(0, END)
    hasil.insert(0, cipher)

def DecryptButton():
    text = plain.get()
    key = int(keyCode.get())
    cipher = ProcessDecrypt(text, key)
    hasil.delete(0, END)
    hasil.insert(0, cipher)

processButtonEncrypt = Button(app, text="Encrypt", command=EncryptButton)
processButtonEncrypt.place(x=10, y=140)
processButtonDecrypt = Button(app, text="Decrypt", command=DecryptButton)
processButtonDecrypt.place(x=10, y=180)

app.geometry('700x350')
app.mainloop()