def inverter():
    numero_invertido = ('')
    for i in numero:
        numero_invertido = i + numero_invertido
    print(f"O Número invertido é:", numero_invertido)

numero = input("Digite um número: ")


inverter()