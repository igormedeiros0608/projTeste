def pot(base, expoente):
    for i in range(1, expoente + 1):
        res = base ** i
        print(f"{base} ** {i} = {res}")

base= int (input("digite a base: "))
expoente = int (input("digite o expoente: "))
pot(base,expoente)

