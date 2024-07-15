######## soma dos algorismos #########
def soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

numero = int(input("Digite um número: "))
resultado = soma_digitos(numero)
print("A soma dos dígitos é:", resultado)

########## nota 3 provas #########
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input(" digite a segunda nota: "))
nota3 = float(input(" digite a terceira nota: "))
media = ( nota1 + nota2 ) + ( nota3 * 2 ) * 10 / 4 
if (media> 59):
    print(f"voce foi aprovado, sua nota foi {media}")
else:
    print(f"voce foi reprovado sua nota foi {media}")

