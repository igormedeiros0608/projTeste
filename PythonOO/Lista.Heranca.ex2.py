class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, cargahora, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.cargahora = cargahora
        self.salario = salario

    def lecionar(self):
        return f"Professor {self.nome} está lecionando {self.disciplina}."


class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return "nota invalida"

aluno1 = Aluno(matricula="1234", nome="Igor ", idade=25, notas=[ 8,9,10])


professor1 = Professor(matricula="777", nome="Thiago", idade=32, formacao= "Analista", disciplina="Algoritimo", cargahora=40, salario=10.000)


print(professor1.lecionar())
print(f"Média do aluno {aluno1.nome} foi de  {aluno1.calcular_media()}")



