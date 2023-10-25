from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("500x250")


def calculate(*args):
    try:
        value1 = float(ent.get())
        value2 = float(enty.get()) / 100
        op = (value1) / (value2 ** 2)
        if op < 16:
            io = 'Выраженный дефицит массы тела'
        elif op < 18.5 and op > 16:
            io = 'Недостаточная (дефицит) масса тела'
        elif op > 18.5 and op < 25:
            io = 'Норма'
        elif op > 25 and op < 30:
            io = 'Избыточная масса тела (предожирение)'
        elif op > 30 and op < 35:
            io = 'Ожирение 1 степени'
        elif op > 35 and op < 40:
            io = 'Ожирение 2 степени'
        elif op > 40:
            io = 'Ожирение 3 степени'
        meters.set(str(op) + ';' + io)

    except ValueError:
        pass


meters = StringVar()
la = ttk.Label(textvariable=meters)

ent = Entry(textvariable='tw')
ent.grid(column=0, row=1, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

o1 = ttk.Label(text='введите массу')
o1.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

enty = Entry(textvariable='tww')
enty.grid(column=0, row=3, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(3, weight=1)

o2 = ttk.Label(text='введите рост')
o2.grid(column=0, row=2, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

o3 = ttk.Label(text='ваш индекс массы; интерпритация:')
o3.grid(column=0, row=4, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(4, weight=1)

la.grid(column=0, row=5, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(5, weight=1)

btn = Button(root, text="Press Enter", command=calculate)
btn.grid(column=0, row=6, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(6, weight=1)

root.bind('<Return>', calculate)
root.mainloop()
