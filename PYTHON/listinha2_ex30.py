valor = float(input("Digite o valor da venda sem empostos: "))
destino = str(input("DIGITE A SIGLA DO ESTADO DE DESTINO, (mg) (sp) (rj) (ms): "))
if(destino == "mg"):
    emposto = valor * 7 /100 + valor
    print(f"O valor com emposto é {emposto}")     
elif(destino == "sp"):
    emposto = valor * 12 /100 + valor
    print(f"O valor com emposto é {emposto}")     
elif(destino == "rj"):
    emposto = valor * 15 /100 + valor
    print(f"O valor com emposto é {emposto}")     
elif(destino == "ms"):
    emposto = valor * 8 /100 + valor
    print(f"O valor com emposto é {emposto}")
else:
    print("estado inesistennte no sistema")     
   