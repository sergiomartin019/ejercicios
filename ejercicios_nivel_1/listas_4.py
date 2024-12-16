asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
asignatura_suspensa =[]
for asignatura in asignaturas:
    nota = float(input(f"introduce tu nota en {asignatura}"))
    if nota <= 5:
        asignatura_suspensa.append(asignatura)


if asignaturas != []:
    print(f"tienes que recuperar {asignatura_suspensa}")