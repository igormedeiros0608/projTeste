######## ex 27 #########
opcao= int(input("Digite uma das opçaoes, 1(adição), 2(diferença entre 2 num), 3(produt 2 num), 4(divisão): "))
if (opcao==1):
    numero1= float(input("digite dois numeros para calcularmos: "))
    numero2= float(input("proximo numero: "))
    res1= numero1 + numero2 
    print(res1)

elif(opcao==2):
    numero1op2= float(input("Digite dois numeros para calcularmos: "))
    numero2op2= float(input("proximo numero: "))
    if(numero1op2>numero2op2):
        res2= numero1op2 - numero2op2
        print(res2)
    else:
        (numero2op2 > numero1op2)
    print(res2)

elif(opcao==3):
    numero1op3= float(input("Digite dois numeros para calcularmos: "))
    numero2op3= float(input("proximo numero: "))
    res3= numero1op3 - numero2op3
    print(res3)

elif(opcao==4):
    numero1op4= float(input("Digite dois numeros para calcularmos: "))
    numero2op4= float(input("proximo numero: "))
    res4= numero1op4 / numero2op4
    print(res4)
        
        
