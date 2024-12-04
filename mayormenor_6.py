numero = float(input("ingresa un primer numero"))
numero2 = float(input("ingresa un segundo numero"))
if numero == numero2:
    print("son iguales")
elif numero > numero2:
    print(f"{numero} es mayor que {numero2}")
else:
    print(f"{numero2} es mayor que {numero}")