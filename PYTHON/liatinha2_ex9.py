### raiz quadrada ####
import math

numero = float(input("digite um numero para calcularmos a raiz: "))
if (numero>0):
    raiz_quadrada = math.sqrt (numero)
    print (raiz_quadrada)
elif (numero < 0 ):
    print(" o numero é negativo ")
