def media(nota1, nota2, nota3, tipo):
    
    if tipo == 'A':
        media = (nota1 + nota2 + nota3) / 3
    elif tipo == 'P':
        media = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
    else:
        "Opção invalida"
    return media

tipo=input("digite o tipo de media desejada: (A) para Aritimetica ou (P) para Ponderada: ")

nota1 =float (input("Digite nota 1: "))
nota2 =float (input("Digite nota 2: "))
nota3 =float (input("Digite nota 3: "))

aritmetica = media(nota1, nota2, nota3, 'A')
ponderada = media(nota1, nota2, nota3, 'P')

print(f"Média Aritmética: {aritmetica}")
print(f"Média Ponderada: {ponderada}")