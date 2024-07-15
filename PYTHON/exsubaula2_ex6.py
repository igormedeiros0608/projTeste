def tabela_e_calcular():
    print("Tabela de Preços:")
    for i in range(1, 51):
        print(f"{i} itens: R$ {i * 1.99}")
    itens= int(input("Digite o número de itens comprados: "))
    valor_total = itens * 1.99
    print(f"O valor total da compra para {itens} itens é: R$ {valor_total}")
tabela_e_calcular()
