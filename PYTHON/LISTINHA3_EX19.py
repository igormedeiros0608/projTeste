numero = int(input("Digite um número inteiro: "))
if numero < 100 or numero >  9999:
    print("numero invalido")
else:
    numero_str = str(numero)
    for digito in numero_str:
        print(digito)