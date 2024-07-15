def financiamento():
    valor= float(input("Qual valor do carro: "))
    entrada= float (input("Qual valor de entrada: "))
    parcelas = int(input("Qual número de parcelas: "))
    finan = valor - entrada
    juros = finan * parcelas / 100
    totalfinan= juros + finan
    valorparcela = totalfinan / parcelas
    print(f"\n valor total: {totalfinan}. \n Valor parcelas: {valorparcela:.2f}.\n Juros:{juros}.")
financiamento()