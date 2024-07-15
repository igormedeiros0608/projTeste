class Pessoa:
    def __init__(self, nome, idade, endereco): #MÉTODO CONSTRUTOR
        self.nome = nome #ATRIBUTO
        self.idade = idade #ATRIBUTO
        self.endereco = endereco #ATRIBUTO

    def mostraNome(self): # METODO/ AÇÃO 
        print(f"NOME: {self.nome}")

    def mostrarIdade(self):
        print(f"IDADE: {self.idade}")
    
    def mostrarEndereco(self):
        print(f"ENDEREÇO: {self.endereco}")

pessoa1 = Pessoa("Igor", "19",  "Rua Capiatã 240")



pessoa1.mostraNome()
pessoa1.mostrarIdade()
pessoa1.mostrarEndereco()