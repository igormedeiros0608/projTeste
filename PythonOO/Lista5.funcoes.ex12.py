def somaEntre(a, b):
    soma = sum(range(a + 1, b))
    
    return soma

num1 = int (input("Digite n1 para fazermos a soma entre os números entre n1 e n2: "))
num2 = int (input("Digite n2 para fazermos a soma entre os números entre n1 e n2: "))
resultado = somaEntre(num1, num2)
print(f"A soma dos números inteiros entre {num1} e {num2} é: {resultado}")