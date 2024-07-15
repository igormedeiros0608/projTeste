def mediaCarro(km, litros):
    consumo = km / litros
    
    if consumo< 8:
        mensagem = "Gasta muito!"
    elif 8 <= consumo <= 15:
        mensagem = "Econômico!"
    else:
        mensagem = "Super econômico"
    
    return f"Consumo: {consumo:.2f} Km/l - {mensagem}"

distancia = float (input("Digite a distancia percorrida:" ))
litros = float (input("Digite a quantidade de litros que foi gasta: "))

print(mediaCarro(distancia, litros))