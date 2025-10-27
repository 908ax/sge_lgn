cad = input("Escribe una cadena: ")
n = int(input("¿Cuántas veces quieres rotarla hacia la izquierda? "))

n = n % len(cad)
nueva_cad = cad[n:] + cad[:n]

print("Cadena rotada:", nueva_cad)