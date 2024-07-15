def calcula_valor(consumo,preco):
    valor = consumo * preco
    return valor

def calcula_consumo(potencia,horas,preco):
    consumo= potencia * horas / 1000
    conta = calcula_valor ( consumo, preco)
    return conta

potencia = int(input("digite a potencia: "))
tempo= int(input("digite o tempo de uso: "))
preco= float(input("digite o preco do kw: "))
banho =calcula_consumo(potencia,tempo,preco)
print(banho)



