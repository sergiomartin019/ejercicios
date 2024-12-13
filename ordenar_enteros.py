def ordena_positivos(lista):
    if lista == []:
        print("esta vacia")
        return lista
    for n in lista:
        if n > 0:
            lista.sort()  
    return lista

lista = [7,5,4,9,3,5,7,3,4,56,7,4,-45]
print(ordena_positivos(lista))
