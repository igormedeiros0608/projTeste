class ContaCorrente:
    def __init__(self, nome, sobrenome, horas, valor):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas = horas
        self.valor = valor

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def salario(self):
        print(f"Voce trabalhou o total de {self.horas} HORAS, e cada hora vale R$: {self.valor} ")
        salario = self.horas * self.valor
        return salario

    def incrementar_horas(self):
        extra = float (input("Digete quantas horas extras vc fez esse mes: "))
        x = extra * self.valor
        return x


funcionario1 = ContaCorrente("João", "Silva", 160, 20)

print(funcionario1.nome_completo()) 

print(funcionario1.salario()) 
print(funcionario1.incrementar_horas())



