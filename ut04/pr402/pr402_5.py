cad = input("Escribe una cadena: ")

nueva_cad = ""
for c in cad:
    if c not in nueva_cad:
        nueva_cad += c

print("Cadena sin caracteres repetidos:", nueva_cad)