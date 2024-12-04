from random import *
def adivinarNumeroRandom():
    intentos = 1
    print("tienes infinitos intentos!!")
    numeroAdivinar = randint(1,100)
    print(numeroAdivinar)
    while True:
        numero = int(input("Adivina el número!"))
        if numero == numeroAdivinar:
            break;
        elif numero > numeroAdivinar:
            print("Pista: el número introducido es mayor que el que tienes que adivinar")
            intentos = intentos +1
        else:
            print("Pista: el número introducido es menor que el que tienes que adivinar")
            intentos = intentos +1
    print("has acertado!")
    print(f"te ha tomado {intentos} intentos!")
adivinarNumeroRandom()

        