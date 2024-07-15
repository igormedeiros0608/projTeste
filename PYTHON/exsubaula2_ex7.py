def sal():
    hora= 10
    carga= float(input("digite horas trabalhadas: "))
    res= hora * carga
    if carga > 40:
        print("vc tem horas extra pra receber ")
        x= carga - 40
        x = x * 10 * (50 /100)
        print(x)
        
    else:
        print("Sem horas extras a receber ")
        
    print(f"Seu salario é : {res + x}")
sal()
