def calculadora(n1,n2,operacao):
    if operacao == "+":
        res1 = n1 + n2 
        print(res1)
    elif operacao == "-":
        res2 = n1 - n2
        print(res2)
    elif operacao == "/":
        res3 = n1 / n2 
        print(res3)
    elif operacao == "*":
        res4 = n1 * n2 
        print(res4)
    
    return operacao

operacao = input( "insira o simbolo da operação desejada (+), (-), (/), (*): ")
n1 = int (input("digite o primeiro numero para o calculo: "))
n2 = int (input("Digite o segundo número: "))

print(calculadora(n1,n2,operacao))