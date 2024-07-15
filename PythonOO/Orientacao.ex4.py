class Conta:
    def __init__(self, nome, CPF, numero, saldo:float):
        self.nome = nome
        self.CPF = CPF
        self.numero = numero
        self.saldo = saldo
    
    def getDados(self):
        print (f"\n NOME: {self.nome} \n CPF:{self.CPF} \n Conta:{self.numero} \n SALDO:{self.saldo}")

    def depositar(self):
        deposito = float(input("digite o valor do deposito: "))
        self.saldo = self.saldo + deposito
        novoSaldo = self.saldo
        return novoSaldo
        
        
    
    def sacar(self):
        saque = float(input("digite o valor do saque: "))
        self.saldo = self.saldo - saque
        novoSaldo2 = self.saldo
        return novoSaldo2

        
conta1 = Conta("jose" , 2423, 23456,100)

conta1.getDados()
print(conta1.depositar())  
print(conta1.sacar())  
conta1.getDados()

