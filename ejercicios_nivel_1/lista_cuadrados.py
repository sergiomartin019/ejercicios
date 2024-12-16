import math
listaCuadrados = []
for i in range(1,11):
    listaCuadrados.append(math.pow(i, 2))
     
print(listaCuadrados)

listaCuadrados2 = [n **2 for n in range(1,11)]
print(listaCuadrados2)