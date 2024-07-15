##### ex 13 ######
numero = float(input("digite um numero: "))  
numero2 = float(input("digite outro numero: "))
if(numero>numero2):
    res = numero - numero2
    print(f"O primeiro numero é maior e sua diferença é {res}")
elif(numero<numero2):
    res2 = numero2 - numero
    print(f"O segundo numero é maior e sua diferenca é {res2}")