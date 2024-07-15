#### fabrica camisa ######

camisap = float( input("QUANTAS CAMISAS P DESEJA: ")) 
camisam = float(input("QUANTAS CAMISAS M DESEJA: "))
cammisag = float(input("QUANTAS CAMISAS G DESEJA: "))

res1 = camisap * 35
res2 = camisam * 45
res3 = cammisag * 55
tot= res1 + res2 + res3

print(f"O valor das camisas P é {res1}, o valor das camisas M é {res2}, e as camisas g {res3}")
print(f" o valor total da compra é {tot} ")

