def verificar (numero):
    if numero >= 1:
        print("numero postivo")
    elif numero == 0 :
        print("Numero neutro (zero)")
    else:
        print("numero negativo")

numero = int (input("digite um número para verificarmos se é positivo, negativo ou neutro: "))
verificar(numero)