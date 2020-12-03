import tkinter as tk
from tkinter import ttk


varaints = {'D-Link': ['DES 1100-06', 'DES 1100-10', 'DES 1210-28', 'DES 1210-52', 'DES 3528',
                       'DGS 1100-06', 'DGS 1100-10', 'DGS 1210-28', 'DGS 1210-52'],
            'Huawei': ['Quidway S2326TP-EI', 'Quidway S2352P-EI'],
            'Cisco': ['C3750']}


def change_depend(event, variant):
    subvariants = varaints[variant]
    combo_depend["values"] = subvariants
    combo_depend.current(0)


app = tk.Tk()
app.geometry('300x200')

labelTop = tk.Label(app, text="Example")
labelTop.place(x=10, y=5)

combo_main = ttk.Combobox(app, values=list(varaints.keys()), state="readonly")
combo_depend = ttk.Combobox(app, values=[], state="readonly")

combo_main.place(x=10, y=30)
combo_depend.place(x=10, y=55)

combo_main.bind("<<ComboboxSelected>>", lambda event: change_depend(event, combo_main.get()))

app.mainloop()
