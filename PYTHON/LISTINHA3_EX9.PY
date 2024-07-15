
menor = float('inf')
maior = float('-inf')  
for i in range(10):
    numero = float(input(f'Digite o {i+1}º número: '))
    if numero < menor:
        menor = numero
    else:
        numero > maior
        maior = numero

print(f"O menor valor lido é: {menor}")
print(f"O maior valor lido é: {maior}")