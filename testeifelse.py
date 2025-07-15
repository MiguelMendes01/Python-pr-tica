import math

a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))
belevado = abs(b)

delta1 = (belevado)**2 - 4*(a)*(c)
delta = math.sqrt(delta1)

bhaskara1 = (-b + delta) / (2 * a)
bhaskara2 = (-b - delta) / (2 * a

print(delta1)
print(bhaskara1)
print(bhaskara2)

if(delta1 > 0):
    print("Existem duas soluções para a equação.")
if(delta1 == 0):
    print("As soluções da equação são repetidas.")
if(delta1 < 0):
    print("Não admite solução real.")
