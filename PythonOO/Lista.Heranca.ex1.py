class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao
    
    def play(self):
        print(f"O filme '{self.nome}' está sendo reproduzido.")

class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
    
    def explodir(self):
        print(f"TIRO, PORRADA E BOMBA em {self.nome}.")

class Drama(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
    
    def chorar(self):
        print(f"CHORA AGORA RI DEPOIS '{self.nome}'.")

class Suspense(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
    
    def suspense(self):
        print(f"{self.nome} Muito suspense pra você!")



filme_acao = Acao("chacina na rocinha", 120)
filme_drama = Drama("O drama das mulheres", 180)
filme_suspense = Suspense("A volta dos que não foram", 130)

filme_acao.play()
filme_acao.explodir()
