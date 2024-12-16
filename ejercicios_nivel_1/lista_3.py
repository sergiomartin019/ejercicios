ganadores = []
for n in range(9):
    numeros = int(input(f"Introduce el {n} numero de la loteria"))
    ganadores.append(numeros)
ganadores.sort()
print(ganadores)

