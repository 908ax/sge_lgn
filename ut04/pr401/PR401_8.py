j1 = input("Di la elección del jugador 1: ").lower()
j2 = input("Di la elección del jugador 2: ").lower()
match j1:
    case "piedra":
        res = ("Gana jugador 1" if j2 in ['lagarto', 'tijeras' ] else
        "Gana jugador 2" if j2 in ['papel', 'spock'] else
        "Empate")
    
    case "papel":
        res = ("Gana jugador 1" if j2 in ['piedra', 'spock' ] else
        "Gana jugador 2" if j2 in ['tijera', 'lagarto'] else
        "Empate")
    case "tijera":
        res = ("Gana jugador 1" if j2 in ['papel', 'lagarto' ] else
        "Gana jugador 2" if j2 in ['piedra', 'spock'] else
        "Empate")
    case "lagarto":
        res = ("Gana jugador 1" if j2 in ['spock', 'papel' ] else
        "Gana jugador 2" if j2 in ['piedra', 'tijera'] else
        "Empate")
    case "spock":
        res = ("Gana jugador 1" if j2 in ['tijera', 'piedra' ] else
        "Gana jugador 2" if j2 in ['papel', 'lagarto'] else
        "Empate")
    case _:
        res = "Elección no válida"
print(res)