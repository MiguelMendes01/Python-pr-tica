import math

a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))

delta = b**2 - 4*a*c

if delta >= 0:
    bhaskara1 = (-b + math.sqrt(delta)) / (2 * a)
    bhaskara2 = (-b - math.sqrt(delta)) / (2 * a)
    if bhaskara1 < bhaskara2:
        print("as raízes da equação são", bhaskara2, bhaskara1)
    if bhaskara2 < bhaskara1:
        print("as raízes da equação são", bhaskara1, bhaskara2)
    if delta == 0:
        print("a raiz desta equação é", bhaskara1)

else:
    print("esta equação não possui raízes reais")





