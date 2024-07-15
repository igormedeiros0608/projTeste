infpessoa = {
    "nome" : "FULANO",
    "idade": "01",
    "cidade" : "CG",
    "profissao" : " Nadador "

}

print(infpessoa)

infpessoa["idade"]= 2

print(infpessoa)

infpessoa['email']= 'fulano_01.com'
print(infpessoa)

infpessoa['numero']= '000-000'
print(infpessoa)

3
#---------------------------------------------
def calculo(item,preco):
    preco = 1.99
    item= int (input("Qual a quantidade de itens:"))
    resultado = item * preco
    return resultado