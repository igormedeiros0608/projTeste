##### ex 18 emprestimo ######
salario = float(input("Digite seu salario: "))
res = ( salario / 100 )* 20 
emprestimo = float(input("Digite o valor do emprestimo desejado: "))
if (emprestimo>res):
    print("EMPRESTIMO NEGADO")
else:
    print("EMPRESTIMO ACEITO ")
