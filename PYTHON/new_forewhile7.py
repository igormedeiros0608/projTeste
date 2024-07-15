numero = int(input("Digite um número inteiro positivo: "))

if numero <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    print("Os primeiros", numero, "números ímpares naturais são:")
    contador = 1
    while numero > 0:
        print(contador)
        contador += 2
        numero -= 1


        