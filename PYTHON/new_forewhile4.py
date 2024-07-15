def calcular_media():
    avaliacao = int(input("Insira o número de avaliações: "))
    soma_notas = 0
    for i in range(avaliacao):
        nota = float(input(f"Insira a nota da avaliação {i + 1}: "))
        soma_notas += nota
    media = soma_notas / avaliacao
    print(f"A média do estudante é: {media}")

calcular_media()









