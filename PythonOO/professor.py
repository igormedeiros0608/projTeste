class Professor:
    def __init__(self, nome, materia, idade, turno): #MÉTODO CONSTRUTOR
        self.nome = nome #ATRIBUTO
        self.materia = materia #ATRIBUTO
        self.idade = idade #ATRIBUTO
        self.turno = turno #ATRIBUTO

    def mostrardados(self): # METODO/ AÇÃO 
        print(f"NOME: {self.nome}")
        print(f"MATERIA: {self.materia}")
        print(f"IDADE: {self.idade}")
        print(f"TURNO: {self.turno}")

Professor1 = Professor ("Thiago", "Programação",25,"Matutino" )
Professor1.mostrardados()
