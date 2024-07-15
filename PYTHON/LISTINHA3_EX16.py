n = int(input("Digite um número inteiro positivo ímpar: "))

if n > 0 and n % 2 != 0:
    print("Números ímpares de 1 até", n, "em ordem crescente:")
    for i in range(1, n + 1, 2):
        print(i)
else:
    print("O número inserido não é um número inteiro positivo ímpar. Tente novamente.")