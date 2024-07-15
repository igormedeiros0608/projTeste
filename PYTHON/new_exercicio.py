numeros= [5,4,3,2,1]
print(len(numeros))
numeros.append(6.1)
numeros.append(7.2)
numeros.append(8.3)
numeros.append(9.4)
numeros.append(10.5)
print(numeros)

numeros.pop()
numeros.pop()
print(numeros)
print(len(numeros))
lista_ordenada = sorted(numeros)
print(lista_ordenada)
print(max(numeros))
print(min(numeros))
lista_decrescente = sorted(numeros, reverse= True)
print(lista_decrescente)
print(sum(numeros))
print(sum(numeros) / len(numeros))
numeros.insert(0, (20))
numeros.insert(1, (30))
print(numeros)
#########################################

#def calcular_media():
    #calcular_media()




