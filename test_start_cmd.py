
vendor = input("Выберите производителя:\n1 - D-Link\n2 - Huawei\n3 - Cisco\n4 - Eltex\n>>> ")
if vendor == '1':                                                                                              # D-Link
    model = input("Выберите модель оборудования:\n1 - DGS 1100-06ME\n2 - DGS 1100-10ME\n3 - DGS 1210-28ME\n"
                  "4 - DGS 1210-56ME\n>>> ")

    if model == '1':  # dgs_1100_06.py
        from switch_config.dgs_1100_06 import config
        print(config)

    elif model == '2':  # DGS 1100-10ME
        from switch_config.dgs_1100_10 import config
        print(config)

    elif model == '3':  # DGS 1210-28ME
        from switch_config.dgs_1210_28 import config
        print(config)

    elif model == '4':  # DGS 1210-52ME
        from switch_config.dgs_1210_52 import config
        print(config)

    elif model == '5':  # DES 1210-52ME
        from switch_config.des_1210_52 import config
        print(config)

    elif model == '6':  # DES 3528
        from switch_config.des_3528 import config
        print(config)

elif vendor == '2':                                                                                            # Huawei
    model = input("Выберите модель оборудования:\n1 - Quidway S2326TP-EI\n2 - Quidway S2352P-EI\n")
    if model == '1':    # Quidway S2326TP-EI
        from switch_config.s2326tp import config
        print(config)

    elif model == '2':  # Quidway S2352P-EI
        from switch_config.s2352p import config
        print(config)

elif vendor == '3':  # Cisco
    model = input("Выберите модель оборудования: ")
    if model == '1':
        pass

    elif model == '2':
        pass

    elif model == '3':
        pass
