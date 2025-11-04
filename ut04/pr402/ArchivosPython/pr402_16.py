cadena = input("Introduce una cadena: ")

palabras = cadena.split()

if not palabras:
    longitud = 0
else:
    longitud = max(len(palabra) for palabra in palabras)

print("La longitud de la palabra más larga es:", longitud)