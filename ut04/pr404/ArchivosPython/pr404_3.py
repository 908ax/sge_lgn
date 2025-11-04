frase = input("Ingresa una frase: ").lower()

palabras = frase.lower().split()

frec = {}

for palabra in palabras:
    if palabra in frec:
        frec[palabra] += 1
    else:
        frec[palabra] = 1

print("La frecuencia de las palabras: ")

for palabra, count in frec.items():
    print(palabra, ": ", count)