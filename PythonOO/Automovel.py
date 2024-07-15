class Automovel:
    def __init__(self,marca,modelo,cor="branco", ano= None, placa="ABC-123"):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.placa = placa
    
    def igar(self):
        print(f" {self.marca} Ligada!!!")

    def getDados(self):
        print(f"Marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"cor: {self.cor}")
        print(f"ano: {self.ano}")
        print(f"placa: {self.placa}")

carro1 = Automovel ("bmw", "320i")
carro1.getDados()





        