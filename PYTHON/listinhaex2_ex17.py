#######nex 17 ########
horas = float (input("Digite suas horas trabalhadas: "))
res = horas * 40.50
if (res<2500):
    print(f" seu salario é {res}")
else:
     res2 = res - (res / 100 ) * 11
print(f"seu salrio com desconto é {res2}")

    

