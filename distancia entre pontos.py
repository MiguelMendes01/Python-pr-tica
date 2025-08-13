import math

x1 = int(input("Insira o primeiro número: "))
y1 = int(input("Insira o primeiro número: "))
x2 = int(input("Insira o primeiro número: "))
y2 = int(input("Insira o primeiro número: "))

distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if distancia >= 10:
    print("longe")
else:
    print("perto")
print(distancia)
