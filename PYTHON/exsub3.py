traducao = {
'hello': 'Hola',
'good morning': 'buen día',
'ate logo':'comió logotipo',
'have a good trip' :'Ten un buen viaje'
}

palavra_ingles = input("Digite uma palavra em inglês: ").strip().lower()

palavra_espanhol = traducao.get(palavra_ingles, "Palavra não encontrada no dicionário")

print(f"A palavra '{palavra_ingles}' em espanhol é: '{palavra_espanhol}'")
