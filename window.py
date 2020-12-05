from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import *
from tkinter.ttk import Label


class Example(Frame):  # окно открывается

    def __init__(self, parent):
        Frame.__init__(self, parent)  # , background="white"
        self.parent = parent
        self.parent.title("Build Config")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):
        w = 520
        h = 250

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        variants = {'D-Link': ['DES 1100-06', 'DES 1100-10', 'DES 1210-28', 'DES 1210-52', 'DES 3528', 'DES 3552',
                               'DGS 1100-06', 'DGS 1100-10', 'DGS 1210-28', 'DGS 1210-52'],
                    'Huawei': ['Quidway S2326TP-EI', 'Quidway S2352P-EI'],
                    'Cisco': ['C3750']}

        def change_depend(variant):
            sub_variants = variants[variant]
            combo_depend["values"] = sub_variants
            combo_depend.current(0)

        labelTop = Label(self, text="Выберите устройство:")
        labelTop.place(x=10, y=5)

        label_vendor = Label(self, text="Фирма:")
        label_vendor.place(x=10, y=30)

        label_model = Label(self, text="Модель:")
        label_model.place(x=10, y=55)

        combo_main = ttk.Combobox(self, values=list(variants.keys()), state="readonly")
        combo_depend = ttk.Combobox(self, values=[], state="readonly")

        combo_main.place(x=80, y=30)
        combo_depend.place(x=80, y=55)

        combo_main.bind("<<ComboboxSelected>>", lambda event: change_depend(combo_main.get()))

        label_ip_address = Label(self, text="ip-address:")  # ip-address:
        label_ip_address.place(x=290, y=30)

        ip_address = Entry(self, bg='white', )  # Поле для ввода "ip-адреса"
        ip_address.place(x=360, y=30)

        label_switch_name = Label(self, text="switch name:")  # switch name:
        label_switch_name.place(x=278, y=60)

        switch_name = Entry(self, bg='white')  # Поле для ввода "имени коммутатора"
        switch_name.place(x=360, y=60)

        label_switch_name = Label(self, text="manager vlan:")  # manager vlan:
        label_switch_name.place(x=273, y=90)

        manager_vlan = Entry(self, bg='white')  # Поле для ввода "менеджер влана"
        manager_vlan.place(x=360, y=90)

        label_switch_name = Label(self, text="untagged vlan:")  # untagged vlan:
        label_switch_name.place(x=269, y=120)

        untagged_vlan = Entry(self, bg='white')  # Поле для ввода "влана в антагете"
        untagged_vlan.place(x=360, y=120)

        label_switch_name = Label(self, text="tagged vlan:")  # tagged vlan:
        label_switch_name.place(x=283, y=150)

        tagged_vlan = Entry(self, bg='white')  # Поле для ввода "вланов в таггете"
        tagged_vlan.place(x=360, y=150)

        def save_config():
            if combo_depend.get() == 'DES 1100-06':
                import switch_config.des_1100_06
                switch_config.des_1100_06.conf(str(ip_address.get()), str(switch_name.get()),
                                               str(manager_vlan.get()), str(untagged_vlan.get()),
                                               str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.des_1100_06.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 'DES 1100-10':
                import switch_config.des_1100_10
                switch_config.des_1100_10.conf(str(ip_address.get()), str(switch_name.get()),
                                               str(manager_vlan.get()), str(untagged_vlan.get()),
                                               str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.des_1100_10.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 'DES 1210-28':
                import switch_config.des_1210_28
                switch_config.des_1210_28.conf(str(ip_address.get()), str(switch_name.get()),
                                               str(manager_vlan.get()), str(untagged_vlan.get()),
                                               str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.des_1210_28.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 'DES 1210-52':
                import switch_config.des_1210_52
                switch_config.des_1210_52.conf(str(ip_address.get()), str(switch_name.get()),
                                               str(manager_vlan.get()), str(untagged_vlan.get()),
                                               str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.des_1210_52.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 'DES 3528':
                import switch_config.des_3528
                switch_config.des_3528.conf(str(ip_address.get()), str(switch_name.get()),
                                            str(manager_vlan.get()), str(untagged_vlan.get()),
                                            str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.des_3528.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 'DES 3552':
                import switch_config.des_3552
                switch_config.des_3552.conf(str(ip_address.get()), str(switch_name.get()),
                                            str(manager_vlan.get()), str(untagged_vlan.get()),
                                            str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.des_3552.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 'DGS 1100-06':
                import switch_config.dgs_1100_06
                switch_config.dgs_1100_06.conf(str(ip_address.get()), str(switch_name.get()),
                                               str(manager_vlan.get()), str(untagged_vlan.get()),
                                               str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.dgs_1100_06.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 'DGS 1100-10':
                import switch_config.dgs_1100_10
                switch_config.dgs_1100_10.conf(str(ip_address.get()), str(switch_name.get()),
                                               str(manager_vlan.get()), str(untagged_vlan.get()),
                                               str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.dgs_1100_10.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 'DGS 1210-28':
                import switch_config.dgs_1210_28
                switch_config.dgs_1210_28.conf(str(ip_address.get()), str(switch_name.get()),
                                               str(manager_vlan.get()), str(untagged_vlan.get()),
                                               str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.dgs_1210_28.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 'DGS 1210-52':
                import switch_config.dgs_1210_52
                switch_config.dgs_1210_52.conf(str(ip_address.get()), str(switch_name.get()),
                                               str(manager_vlan.get()), str(untagged_vlan.get()),
                                               str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.dgs_1210_52.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 's2336tp':
                import switch_config.s2326tp
                switch_config.s2326tp.conf(str(ip_address.get()), str(switch_name.get()),
                                           str(manager_vlan.get()), str(untagged_vlan.get()),
                                           str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.s2326tp.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 's2352p':
                import switch_config.s2352p
                switch_config.s2352p.conf(str(ip_address.get()), str(switch_name.get()),
                                          str(manager_vlan.get()), str(untagged_vlan.get()),
                                          str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.s2352p.config2
                f.write(s)
                f.close()

            elif combo_depend.get() == 'c3750':
                import switch_config.c3750
                switch_config.c3750.conf(str(ip_address.get()), str(switch_name.get()),
                                         str(manager_vlan.get()), str(untagged_vlan.get()),
                                         str(tagged_vlan.get()))
                file_name = fd.asksaveasfilename()
                file_txt = str(file_name) + '.txt'
                f = open(file_txt, 'w')
                s = switch_config.c3750.config2
                f.write(s)
                f.close()

        # Кнопка Сбора конфига
        btn = Button(self, width=18, height=2, text="Сохранить конфиг", command=save_config, relief=GROOVE)
        btn.place(x=180, y=195)


def main():
    root = Tk()
    root.resizable(False, False)
    # root.iconbitmap('icon.ico')
    Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()

