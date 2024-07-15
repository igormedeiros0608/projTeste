def temperatura(c):
    F = c * (9.0/5.0) + 32.0
    return F

c= float(input("Digite graus celsios para convertemos em Fahrenheit: "))
print(temperatura(c))