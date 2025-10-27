cad = input("Escribe una cadena: ")

nueva_cad = ""
for c in cad:
    if c.islower():
        nueva_cad += c.upper()
    elif c.isupper():
        nueva_cad += c.lower()
    else:
        nueva_cad += c

print("Cadena con mayúsculas y minúsculas invertidas:", nueva_cad)