class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def mostrarpag(self):
        return self.paginas
    
    def getEditora(self):
        return self.editora 
    
    def alterarEditora(self, novaEditora):
        self.editora = novaEditora

    def mostraDados(self): 
        print(f"NOME: {self.nome} Autor: {self.autor} Editora: {self.editora} ")

livro1 = Livro (f"A voz da Alma", "Caleb Couto", "Leitura", 777)
livro1.alterarEditora("Basil Central")


print(livro1.mostrarpag())
print(livro1.mostraDados())


