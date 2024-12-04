
def adivinarNumero(numeroAdivinarI, intentoI):
    numeroAdivinar = numeroAdivinarI
    intento = intentoI
    adivinado = False
    while intento != 0:
        print(f"tienes {intento} intentos!")
        numero = int(input("Adivina el número!"))
        if numero == numeroAdivinar:
            adivinado = True;
            break;
        else:
            intento = intento - 1
    if adivinado:
        print("has acertado!")
    else:
        print("Has perdido, no hay mas intentos!")

def adivinarNumeroInfinito(numeroAdivinarI):
    print("tienes infinitos intentos!!")
    numeroAdivinar = numeroAdivinarI
    while True:
        numero = int(input("Adivina el número!"))
        if numero == numeroAdivinar:
            break;
    print("has acertado!")
    
    

adivinarNumero(7, 10)
adivinarNumeroInfinito(7)

    
    
    


