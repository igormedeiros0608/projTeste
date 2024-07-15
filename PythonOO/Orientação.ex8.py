class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120.00):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def IMC(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def valor_mensalidade(self):
        if self.idade < 18:
            desconto = self.mensalidade * 0.20
            return self.mensalidade - desconto
        else:
            return self.mensalidade

def aluno1():
    nome = input("Informe o nome do aluno: ")
    idade = int(input("Informe a idade do aluno: "))
    peso = float(input("Informe o peso (em kg): "))
    altura = float(input("Informe a altura (em metros): "))

    aluno = AlunoAcademia(nome, idade, peso, altura)

    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Peso: {aluno.peso} kg")
    print(f"Altura: {aluno.altura} m")
    print(f"IMC: {aluno.IMC():.2f}")
    print(f"Valor da mensalidade: R$ {aluno.valor_mensalidade()}")

aluno1()
