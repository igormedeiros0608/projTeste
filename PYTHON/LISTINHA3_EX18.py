quantidade = int(input("Digite a quantidade de números a serem lidos: "))

if quantidade > 0:
    maior_numero = 0
    for i in range(quantidade):
        numero = int(input(f"Digite o número {i + 1}: "))
        
        if maior_numero is 0 or numero > maior_numero:
            maior_numero = numero

    print("O maior número é:", maior_numero)
else:
    print("A quantidade de números deve ser um número inteiro positivo.")
