#### brecho ex 7 #########
num1 = float (input("qual valor da compra: "))
if (num1 >50):
    res= (num1 /100) * 45 + num1
    print(f" esse produto deve ser vendido 45% acima do valor de compra {res}")
elif(num1 < 50):
    res= (num1 /100) * 30 + num1
    print(f" esse produto deve ser vendido 30% acima do valor de compra {res}")

