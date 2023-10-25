from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x250")


def calculate(*args):
    try:
        value = ent.get()  # используем геттер для объекта StringVal

        meters.set(eval(value))  # используем сеттер для объекта StringVal

    except ValueError:
        pass


meters = StringVar()
la = ttk.Label(textvariable=meters)

ent = Entry()
ent.pack()
la.pack()
btn = Button(root, text="Press Enter", command=calculate)
btn.pack(ipadx=50)
root.bind('<Return>', calculate)
root.mainloop()