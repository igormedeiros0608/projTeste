def estacionamento():
    hr1 = 9.0
    horas = float (input("Quantas horas ficou no estacionamento: "))
    if horas > (0.16):
        adicional = 1.5
        res = hr1 + adicional * horas - 1.5
        cofins = ( res / 100) * 0.20
        pis = (res / 100) * 0.33
        icms = (res / 100) * 17
        print(f"\n valor total: {res}. \n COFINS: {cofins}.\n PIS:{pis}. \n ICMS:{icms}")
    elif horas <= (0.15):
        print("Estacionamento sem custo, ate a proxima ")
    else:
        hr1 
        cofins = ( hr1 / 100) * 0.20
        pis = (hr1 / 100) * 0.33
        icms = (hr1 / 100) * 17
        print(f"\n valor total: {hr1}. \n COFINS: {cofins}.\n PIS:{pis}. \n ICMS:{icms}")
estacionamento()

