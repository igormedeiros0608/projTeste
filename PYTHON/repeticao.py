frutas = ["maca", "kiwi", "manga", "tomate", "banana", "cereja"]
for item in frutas:
    print(item)

    ##########################################################
###################################################################

contador= 0
while(contador < 5):
    print(contador)
    contador = contador + 1

###########################################################3

x = 0 
soma = 0 
while x <=10:
    soma = soma + x
    x = x + 1

print(soma)

##############################################################
nova_lista= [45, 8, 29, 27, 22, 39]
position = 3
i= 0 
j= 1
print(nova_lista [j])

###############################################################

numeros = [2, 3, 4, 11, 5]
i = 0
while i <len(numeros):
    print(numeros[i])
    if numeros[i] == 11:
        print("encontramos o numero 11 !")
        break
    else:
        i = i + 1