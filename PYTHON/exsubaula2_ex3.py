def quantidade_de_digitos():
    numero = int(input("Por favor, insira um número inteiro: "))
    quantidade = len(str((numero)))
    print(f"O número {numero} tem {quantidade} dígitos.")

quantidade_de_digitos()
