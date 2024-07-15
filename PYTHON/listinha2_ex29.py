def eh_bissexto(ano):
    if (ano % 400 == 0 ) or (ano % 4 == 0 and ano % 100 !=0):
        return True
    else:
        return False
    
ano = int (input("Digite o ano: "))

if eh_bissexto(ano):
    print(f"{ano}, é um ano bissesxto.")
else:
    print(f"{ano}, não é bissexto. ")