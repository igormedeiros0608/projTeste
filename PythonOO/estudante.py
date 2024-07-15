class Estudante:
    def __init__(self, matricula, nome, idade, nota): #MÉTODO CONSTRUTOR
        self.matricula = matricula #ATRIBUTO
        self.nome = nome #ATRIBUTO
        self.idade = idade #ATRIBUTO
        self.nota = nota #ATRIBUTO

    def hello(self): # METODO/ AÇÃO 
        print(f"ola {self.nome}")


aluno = Estudante(1212,"pedro", 18,80)
print(aluno.nome)


        
