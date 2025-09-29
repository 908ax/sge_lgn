from random import *

print("Opciones: piedra, papel, tijeras, lagarto, spock")

jugador = 0
maquina = 0

while jugador < 5 and maquina < 5:
    eleccion = input("Tu elección: ")
    pc = choice(["piedra","papel","tijeras","lagarto","spock"])
    print("La máquina eligió:", pc)

    if eleccion == pc:
        print("Empate")

    elif eleccion == "piedra" and (pc == "tijeras" or pc == "lagarto"):
        print("Ganaste esta mano")
        jugador += 1
    elif eleccion == "papel" and (pc == "piedra" or pc == "spock"):
        print("Ganaste esta mano")
        jugador += 1
    elif eleccion == "tijeras" and (pc == "papel" or pc == "lagarto"):
        print("Ganaste esta mano")
        jugador += 1
    elif eleccion == "lagarto" and (pc == "spock" or pc == "papel"):
        print("Ganaste esta mano")
        jugador += 1
    elif eleccion == "spock" and (pc == "tijeras" or pc == "piedra"):
        print("Ganaste esta mano")
        jugador += 1
    else:
        print("Gana la máquina esta mano")
        maquina += 1

    print("Marcador -> Tú:", jugador, " Máquina:", maquina)

if jugador == 5:
    print("¡Felicidades, ganaste la partida!")
else:
    print("La máquina ganó la partida :(")