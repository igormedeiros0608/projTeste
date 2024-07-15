numero = int(input("Digite um numero: "))
numero_impar = 1
lista = []
if (numero > 0):
    for i in range (numero):
        lista.append(numero_impar)
        dec = sorted(lista, reverse= True)
        numero_impar = numero_impar + 1 
    dec.append(0)
    for item in dec:
        print(item)
else:
    print("numero invalido")
