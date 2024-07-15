def armazenar_dados(**kwargs):
    dados_pessoa = kwargs
    for chave in dados_pessoa():
    
        print(f"{chave}: {dados_pessoa}")


nome= input("digite seu nome: ")
idade=input("digite sua idade: ")
cidade= input("digite sua cidade: ")
profissao= input("digite sua profissao: ")

armazenar_dados




