numero = int(input("Digite um número inteiro: "))
soma = 0
for i in range(1, numero):
    if numero % i == 0:
        soma = soma + i
print(f"A soma dos divisores de {numero}, excluindo ele próprio, é: {soma}")