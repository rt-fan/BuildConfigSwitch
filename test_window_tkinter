from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.ttk import Label


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)  # , background="white"
        self.parent = parent
        self.parent.title("Окно по центру экрана")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self, tk=None):
        w = 520
        h = 400

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # quitButton = Button(self, text="Закрыть окно", command=self.quit)
        # quitButton.place(x=10, y=150)

        # comboExample = ttk.Combobox(self, values=[ "January", "February", "March", "April"], state="readonly")
        #
        # comboExample.grid(column=0, row=1)
        # comboExample.current(0)

        varaints = {'D-Link': ['DES 1100-06', 'DES 1100-10', 'DES 1210-28', 'DES 1210-52', 'DES 3528', 'DES 3552',
                               'DGS 1100-06', 'DGS 1100-10', 'DGS 1210-28', 'DGS 1210-52'],
                    'Huawei': ['Quidway S2326TP-EI', 'Quidway S2352P-EI'],
                    'Cisco': ['C3750']}

        def change_depend(event, variant):
            subvariants = varaints[variant]
            combo_depend["values"] = subvariants
            combo_depend.current(0)

        labelTop = Label(self, text="Выберите устройство:")
        labelTop.place(x=10, y=5)

        label_vendor = Label(self, text="Фирма:")
        label_vendor.place(x=10, y=30)

        label_model = Label(self, text="Модель:")
        label_model.place(x=10, y=55)

        combo_main = ttk.Combobox(self, values=list(varaints.keys()), state="readonly")
        combo_depend = ttk.Combobox(self, values=[], state="readonly")

        combo_main.place(x=80, y=30)
        combo_depend.place(x=80, y=55)

        combo_main.bind("<<ComboboxSelected>>", lambda event: change_depend(event, combo_main.get()))

        label_ip_address = Label(self, text="ip-address:")  # ip-address:
        label_ip_address.place(x=290, y=30)

        ip_address = Entry(self, bg='white',)  # Поле для ввода "ip-адреса"
        ip_address.place(x=360, y=30)

        label_switch_name = Label(self, text="switch name:")  # switch name:
        label_switch_name.place(x=278, y=60)

        switch_name = Entry(self, bg='white')  # Поле для ввода "имени коммутатора"
        switch_name.place(x=360, y=60)

        label_switch_name = Label(self, text="manader vlan:")  # manader vlan:
        label_switch_name.place(x=273, y=90)

        manager_vlan = Entry(self, bg='white')  # Поле для ввода "менеджер влана"
        manager_vlan.place(x=360, y=90)

        label_switch_name = Label(self, text="untagged vlan:")  # untagged vlan:
        label_switch_name.place(x=269, y=120)

        untegged_vlan = Entry(self, bg='white')  # Поле для ввода "влана в антагете"
        untegged_vlan.place(x=360, y=120)

        label_switch_name = Label(self, text="tagged vlan:")  # tagged vlan:
        label_switch_name.place(x=283, y=150)

        tagged_vlan = Entry(self, bg='white')  # Поле для ввода "вланов в таггете"
        tagged_vlan.place(x=360, y=150)


        def save_config():
            if combo_depend.get() == 'DES 1100-06':
                from switch_config.test import config
                print(str(ip_address.get() + config))

            file_name = fd.asksaveasfilename(
                filetypes=(("TXT files", "*.txt"),
                           ("HTML files", "*.html;*.htm"),
                           ("All files", "*.*")))
            f = open(file_name, 'w')
            s = config
            f.write(s)
            f.close()


        # button_save = Button(self, text='Click to Open File', command=save_config)
        # button_save.place(x=200, y=200)

        # text = Text(self, width=50, height=1)
        # text.grid(columnspan=2)

        btn = Button(self, text="Сохранить конфиг", command=save_config)  # Кнопка Сбора конфига
        btn.place(x=10, y=85)

        # def but():
        #     print(combo_depend.get())

        # btn2 = Button(self, text='кнопка', command=but)
        # btn2.place(x=10, y=100)

def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
