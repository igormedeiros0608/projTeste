class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def mostrar_setor(self):
        return f"Setor do ingresso: {self.setor}"


class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote=False, open_bar=False, open_food=False, estacionamento=False):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def bebida(self):
        if self.open_bar:
            return "Pegando bebida no open bar."
        else:
            return "Este ingresso não tem open bar."

    def camarote(self):
        if self.camarote:
            return "Acessando o camarote."
        else:
            return "Este ingresso não dá acesso ao camarote."




ingresso_comum = Ingresso(preco=50.0, setor="Arquibancada")
print(ingresso_comum.mostrar_setor())
ingresso_comum.alterar_preco(55.0)
print(f"Novo preço do ingresso: {ingresso_comum.preco}")


ingresso_vip = IngressoVIP(preco=150.0, setor="Camarote", camarote=True, open_bar=True, open_food=True, estacionamento=True)
print(ingresso_vip.mostrar_setor())
print(ingresso_vip.bebida())
print(ingresso_vip.camarote())
 