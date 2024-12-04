import random
def Usuario_Elegir():
    eleccion = input("escribe piedra, papel o tijera").lower()
    return eleccion

def MaquinaElegir():
    lista = ["piedra", "papel", "tijera"]
    return random.choice(lista)

def piedra_papel_tijera():
    eleccion_usuario = Usuario_Elegir()
    maquina = MaquinaElegir()
    match eleccion_usuario:
        case "piedra":
            if maquina == "papel":
                print("has perdido")
            elif maquina == "tijera":
                print("has ganado")
            else:
                print("empate")
        case "papel":
            if maquina == "tijera":
                print("has perdido")
            elif maquina == "piedra":
                print("has ganado")
            else:
                print("empate")
        case "tijera":
            if maquina == "piedra":
                print("has perdido")
            elif maquina == "papel":
                print("has ganado")
            else:
                print("empate")
        case _:
            print("elige de nuevo")
            piedra_papel_tijera()
            
piedra_papel_tijera()
            