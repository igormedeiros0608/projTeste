def potencia(x, z):
    resultado = 1
    
    for i in range(z):
        resultado *= x
        
    return resultado

x = 3
z = 4
resultado = potencia(x, z)
print(f"O resultado de {x} elevado a {z} é: {resultado}")