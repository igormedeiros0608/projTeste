def listinha(tamanho , valor_padrao):
    return [valor_padrao] * tamanho

tamanho = int(input("Qual tamanho da lista que deseja: "))     
valor_padrao = int(input("Digite o valor padrão: ")) 
lista = listinha(tamanho , valor_padrao)
print(lista)
listinha(tamanho, valor_padrao)
