pares = 0
impares = 1

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
for numero in range(numero1, numero2 + 1):
    if numero % 2 == 0:
        pares = numero + pares
    else:
        impares = numero * impares

print("A soma dos números pares é:", pares)
print("A multiplicação dos números ímpares é:", impares)

