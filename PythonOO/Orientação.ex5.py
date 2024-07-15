class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def imprimir_raio(self):
        print(f"Raio: {self.raio}")

    def area(self):
        return 3.14 * (self.raio ** 2)

    def circunferencia(self):
        return 2 * 3.14 * self.raio

circulo = Circulo(10)
circulo.imprimir_raio()
print(f"ÁREA: {circulo.area()}")
print(f"CIRCUFERENCIA : {circulo.circunferencia()}")