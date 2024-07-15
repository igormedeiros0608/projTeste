######## ex 26 ######
a= float(input("Digite a primeira medida: "))
b= float(input("Digite a segunda medida: "))
c= float(input(" Digite o terceira medida: "))
if(a != b  != c):
    print("ESCALENO")
elif( a == b == c):
    print("EQUILATERO")
elif(a == b or b == a or c == a or a == c or b == c or c == b):
    print("ISOSCELES")
else:
    print("ERROR404")
