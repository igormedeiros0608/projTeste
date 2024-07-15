class Carro:
    def __init__(self, modelo, marca, cor, ano, valor, consumo, nivel:float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo  
        self.nivel = nivel
    
    def abastecer(self, litros):
        litros = float (input("Qauntos litros deseja abastecer: "))
        gas = self.nivel + litros
        self.nivel += litros  
        gas = gas
        print(f'Abastecido com {litros} litros. Nível atual: {self.nivel} litros.')
    
    def media(self):
        distancia = float (input("Digite a distancia que deseja percorrer em km:  "))
        media = distancia / self.consumo 
        media = media
        print(f'Para percorrer {distancia} km. O carro ira gastar uma media de {media} litros')



    def verificar_nivel(self):
        print(f'Nível atual do tanque: {self.nivel:.2f} litros.')
        return self.nivel
    
    def calcular_imposto(self):
        ipva = self.valor * 0.025
        print(f'O valor do IPVA é: R$ {ipva:.2f}')
        return ipva

carro1 = Carro('911', 'Porsche', 'Verde', 2024, 1500000, 10, 20)

carro1.abastecer(0)

carro1.verificar_nivel()

carro1.media()

carro1.calcular_imposto()   