from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from random import choice
import pyperclip


win = ThemedTk(theme='equilux')
win.configure(themebg='equilux')
win.title('Password Generator')

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!@#$%^&*()'

def generate():
    txt.delete(0, END)
    pass_type = rdbt.get()
    length = int(cmb.get())

    password = ''
    c = ''

    if pass_type == 1:
        c = letters
    elif pass_type == 2:
        c = letters + numbers
    elif pass_type == 3:
        c = letters + numbers + symbols

    for i in range(length):
        character = choice(c)
        password += character

    txt.insert(0, password)

def encrypt():
    key = 4
    encrypted_pass = ''

    pass_type = rdbt.get()
    password = txt.get()

    if pass_type == 1:
        a = letters
        for i in range(len(password)):
            index = a.find(password[i])
            letter = (index + key) % len(a)
            encrypted_pass += a[letter]
    elif pass_type == 2:
        a = letters + numbers
        for i in range(len(password)):
            index = a.find(password[i])
            letter = (index + key) % len(a)
            encrypted_pass += a[letter]
    elif pass_type == 3:
        a = letters + numbers + symbols
        for i in range(len(password)):
            index = a.find(password[i])
            letter = (index + key) % len(a)
            encrypted_pass += a[letter]

    txt.delete(0, END)
    txt.insert(0, encrypted_pass)


def copy_pass():
    pyperclip.copy(txt.get())

rdbt = IntVar()

title = ttk.Label(win, text="Password Generator")

rdb = ttk.Radiobutton(win, text="Easy",  variable=rdbt, value=1)
rdb2 = ttk.Radiobutton(win, text="Medium",  variable=rdbt, value=2)
rdb3 = ttk.Radiobutton(win, text="Hard",  variable=rdbt, value=3)

lbl = ttk.Label(win, text="Length")
cmb = ttk.Combobox(win)
cmb["values"] = ("8", "16")
cmb.set('8')

lbl2 = ttk.Label(win, text="   Password   ")
txt = ttk.Entry(win, width=20, font=('Calibri', 10))
btn = ttk.Button(win, text="Generate", command = generate)
enc = ttk.Button(win, text="Encrypt", command = encrypt)
copy = ttk.Button(win, text="Copy", command = copy_pass)

title.grid(row=0,column=0,columnspan=3)

rdb.grid(row=1, column=0)
rdb2.grid(row=1, column=1)
rdb3.grid(row=1, column=2)

lbl.grid(row=2, column=0)
cmb.grid(row=2, column=1)

lbl2.grid(row=3, column=0)
txt.grid(row=3, column=1)
btn.grid(row=4, column=1)
enc.grid(row=5, column=1)
copy.grid(row=6, column=1)



win.mainloop()

