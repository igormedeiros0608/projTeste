##### ex 35 cosmiisao 700 ++++ #####
venda= float(input("valor da venda: "))
if (venda >= 1000000):
    comissao= (venda *16 / 100 ) + 700
    print(comissao)
elif (venda < 100000 and venda >= 80000):
    comissao = (venda * 14 / 100) + 650
    print(comissao)
elif (venda < 100000 and venda >= 60000):
    comissao = (venda * 14 / 100) + 600
    print(comissao)
elif (venda < 100000 and venda >= 40000):
    comissao = (venda * 14 / 100) + 550
    print(comissao)
elif (venda < 100000 and venda >= 20000):
    comissao = (venda * 14 / 100) + 500
    print(comissao)
else:
    comissao = (venda * 14 / 100)
    print(comissao)