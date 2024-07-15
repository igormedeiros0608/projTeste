def verificar_sinal():
    numero = float(input("Por favor, insira um número: "))
    if numero > 0:
        return 'p'
    elif numero <=0:
        return 'n'
resultado = verificar_sinal()
print(f"O resultado é: {resultado}")