n = int(input("Digite um número inteiro positivo par: "))

if n > 0 and n % 2 == 0:
    print("Números pares de 0 até", n , "em ordem crescente:")
    for i in range(0, n + 1, 2):
        print(i)
else:
    print("O número inserido não é um número inteiro positivo par. Tente novamente.")