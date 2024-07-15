
totalnum = 0
pares = 0
while True:
    numero = int(input("Digite um número inteiro (digite 0 para encerrar): "))
    if numero == 0:
        break
    totalnum += 1
    if numero % 2 == 0:
        pares += 1
print("Total de números lidos:", totalnum)
print("Número de valores pares:", pares)