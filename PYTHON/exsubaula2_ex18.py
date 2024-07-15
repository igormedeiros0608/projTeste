def desconto_churras(dia, valor):
    dia= (input("digite o dia da semana: "))
    valor= (input("digite o valor: "))
    if dia == (segunda):
        segunda = (valor + valor * 0.10) 
    if dia == (terca):
        terca = (valor + valor * 0.10) - ( valor / 100) * 0.10
    if dia == (quarta):
        quarta = (valor + valor * 0.10) -  ( valor / 100) * 0.15
    if dia == (quinta):
        quinta = (valor + valor * 0.10) - ( valor / 100) * 0.20
    if dia == (sexta):
        sexta = (valor + valor * 0.10) 
    if dia == (sabado):
        sabado = (valor + valor * 0.10) 
    print(f"{dia}: {valor}")
desconto_churras
