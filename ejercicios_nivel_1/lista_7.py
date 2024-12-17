palabra = input("introduce una palabra: ").lower()

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for chr in palabra:
    if chr == "a":
        contador_a = contador_a + 1
    elif chr == "e":
        contador_e = contador_e + 1
    elif chr == "i":
        contador_i = contador_i + 1
    elif chr == "o":
        contador_o = contador_o + 1
    elif chr == "u":
        contador_u = contador_u + 1
        
print("aparece la a: ", contador_a)
print("aparece la e: ", contador_e)
print("aparece la i: ", contador_i)
print("aparece la o: ", contador_o)
print("aparece la u: ", contador_u)