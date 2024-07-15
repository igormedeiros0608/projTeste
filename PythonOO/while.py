i = 0
soma = 0
while i < 10:
    try:
        x = int(input("DIGITE UM NÚMERO: "))
        soma += x
        i += 1
    except:
        print("VALOR INVALIDO, TENTE NOVAMENTE")

print(soma)
