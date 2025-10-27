cad = input("Escribe una cadena: ").title().replace(" ", "").replace("-", "")

cad = cad[0].lower() + cad[1:]

print(cad)