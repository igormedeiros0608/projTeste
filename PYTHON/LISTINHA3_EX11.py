soma = 0
contador = 0

for numero in range(0, 101, 2):
    soma += numero
    contador += 1
    if contador == 50:
        break

print("A soma dos 50 primeiros números pares é:", soma)