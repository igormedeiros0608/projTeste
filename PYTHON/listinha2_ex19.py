#### ex 19 #####
sexo = str (input("digite seu sexo: "))
altura = float (input("difite sua altura: "))
if sexo.upper() == "F": 
    print("f - feminino")
    res = (62.1 * altura) - 58
    print(res)
elif sexo.upper()== "M":
    print("m - masculino")
    res2 = (72.7 * altura) - 44.7
    print(res2)



