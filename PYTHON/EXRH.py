import sys
nome = str(input("Digite seu nome completo: "))
cargo = str(input("Qual cargo desejado: "))
email = str(input("Digite seu email: "))
idade = int(input("Digite sua idade: "))
if(idade>=18):
    print(f"VOCE ESTA APTO PARA PROXIMA FASE, ENVIAMOS EM SEU EMAIL")
elif(idade<18):
    print(f"OBRIGADO PELA PARTICIPAÇÃO")
    sys.exit()
qualificacao = str(input("Possui qualificação na area? Digite sim ou não: "))
if(qualificacao == "sim"):
    print(f"VOCE ESTA APTO PARA PROXIMA FASE, ENVIAMOS EM SEU EMAIL")
else:
    print("OBRIGAO PELA PARTICIPAÇÃO")
nota = float(input("Digite a nota da sua avaliação feita em sala: "))
if(nota>7):
        print(f"PARABENS VOCE FOI APROVADO, ENVIAREMOS OS PASSOS A SEGUIR EM {email}")
else:
     print("OBRIGADO PELA PARTICIPAÇÃO")

