def pesca():
    kg = float(input("Quantos kg de peixes foi pescado: "))
    if kg > (50):
        print("Você escedeu o limite ")
        x= kg - 50
        print(f"O valor ultapassado foi: {x} kilos")
        x = x * 4   
        print(f"O valor de multa a ser pago é :{x}")
    else:
        print("não ha taxa")
pesca()