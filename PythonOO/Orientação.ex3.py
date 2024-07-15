class Aluno:
    def __init__(self, nome, RA, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.RA = RA
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
    
    def mostrarDados(self):
        print(f"NOME: {self.nome} RA: {self.RA}")

        

    def mostraSituacao(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        if media<=(4.9):
            return "REPROVADO"
        elif media>= (5.0) and media <= (6.9):
            return "EXAME"
        else:
            print("APROVADO")
        return media
    
aluno1 = Aluno ("jose" , "2423", 8 , 9, 7, 8)

print(aluno1.mostrarDados())
print(aluno1.mostraSituacao())


