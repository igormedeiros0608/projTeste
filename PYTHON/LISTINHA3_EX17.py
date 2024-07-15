numero = int(input("Digite um número inteiro positivo: "))
if numero > 0:
    soma = sum(range(1, numero + 1))
    print("A soma dos", numero, "primeiros números naturais é:", soma)
else:
    print("O número inserido não é um número inteiro positivo. Tente novamente.")