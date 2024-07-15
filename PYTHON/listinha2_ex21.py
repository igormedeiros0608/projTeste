###### meida #######
nota1 = float(input("digite a primeira nota, trbalho de laboratorio: "))
nota2 = float(input(" digite a segunda nota, avaliação semestral: "))
nota3 = float(input(" digite a terceira nota, exame final: "))
media = ( nota1 * 3) +(nota2 * 3) + ( nota3 * 5) / 3
if (media<3.0):
    print(f"voce foi reprovado, sua media foi {media}")
elif (media<6.0):
    print(f"voce esta de exame, sua media foi {media}")
else:
    print(f"voce foi aprovado sua media foi {media}")