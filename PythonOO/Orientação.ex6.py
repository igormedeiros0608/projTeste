class Agenda:
    def __init__(self):
        self.anotacoes = []

    def anotacao(self):
        dia = input("Digite o dia: ")
        mes = input("Digite o mês: ")
        ano = input("Digite o ano: ")
        anotacao = input("Digite a anotação: ")
        self.anotacoes.append((dia, mes, ano, anotacao))

    def mostrarAnotacoes(self):
        for dia, mes, ano, anotacao in self.anotacoes:
            print(f"Data: {dia}/{mes}/{ano} - Anotação: {anotacao}")

agenda = Agenda()
agenda.anotacao()
agenda.mostrarAnotacoes()
