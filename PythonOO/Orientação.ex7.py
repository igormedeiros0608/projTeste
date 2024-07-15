class Triangulo:
    def __init__(self, ladoA,ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB =ladoB
        self.ladoC = ladoC

    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def getMaiorLado(self):
        return max(self.ladoA, self.ladoB, self.ladoC)

def criar_triangulo():
    ladoA = float(input("Informe Lado A: "))
    ladoB = float(input("Informe Lado B: "))
    ladoC = float(input("Informe Lado C: "))

    triangulo = Triangulo(ladoA,ladoB,ladoC)

    print(f"Perímetro do triângulo: {triangulo.perimetro()}")
    print(f"Maior lado do triângulo: {triangulo.getMaiorLado()}")

criar_triangulo()