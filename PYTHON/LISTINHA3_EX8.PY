lista = 0
contador = 0 
soma= 0 
while contador < 10:
    lista = int(input("digite um numero para realizarmos a media deles: " ))
    if lista < 0:
        print("insira um numero postivo")
    else:
        contador = contador +1
        soma = soma + lista
        res = soma / 10
   
print(res)