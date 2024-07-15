estoque = {
    'chave' : '15',
    'portas':  '20',
    'janelas': '30',

}
for item in sorted(estoque):
    print (item, estoque [item])

produto = input("Digite o nome do produto que deseja verificar: ").strip().lower()

if produto in estoque:
    quantidade = estoque[produto]
    print(f"Temos {quantidade} unidades de {produto} em estoque.")
else:
    print(f"O produto '{produto}' não está disponível em nosso estoque.")






  