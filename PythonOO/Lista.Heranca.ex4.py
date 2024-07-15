class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def escolher_assento(self, novo_assento):
        self.assento = novo_assento

class PassagemAviao(Passagem):
    def __init__(self, preco, assento, embarque, checkin):
        super().__init__(preco, assento)
        self.embarque = embarque
        self.checkin = checkin

    def decolar(self):
        return f"Avião decolando do portão {self.embarque}."


class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def partida(self):
        return f"Ônibus partindo com placa {self.placa}."


passAviao = PassagemAviao(preco=500.0, assento="A12",embarque="G7", checkin=True)
print(f"Preço da passagem de avião: {passAviao.preco}")
print(f"Assento escolhido: {passAviao.assento}")
print(passAviao.decolar())



passOnibus = PassagemBus(preco=100.0, assento="12B", placa="XYZ1234", leito=True)
print(f"Preço da passagem de ônibus: {passOnibus.preco}")
print(f"Assento escolhido: {passOnibus.assento}")
print(passOnibus.partida())
