class Pessoa:
    def __init__(self,id= 0, nome= ""):
        self.id = id
        self.nome = nome


    def hello(self):
        print(f"Óla {self.nome}")

pessoa1= Pessoa()

print(pessoa1.id)

print("BOM DIA")
name= input ("Digite seu nome")

pessoa1.nome = name

pessoa1.hello()
