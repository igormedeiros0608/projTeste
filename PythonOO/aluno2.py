class Aluno:
    def __init__(self, nome, RA, notas):
        self.nome = nome
        self.RA = RA
        self.notas = notas    

    def mostrarsituacao(self):
        media = sum(self.notas) / len(self.notas)
        

        if media <=(4.9):
            return "REPROVADO"
        elif media>= (5.0) and media <= (6.9):
            return "EXAME"
        else:
            return "APROVADO"
    
notas = []
nome = input ("Digite o nome: ")
ra = int(input("digite o ra: "))

i = 0
while i < 4:
    nota = float(input("nota: "))
    notas.append(nota)
    i = i + 1

aluno1 = Aluno (nome,ra,notas)

print(aluno1.mostrarsituacao())