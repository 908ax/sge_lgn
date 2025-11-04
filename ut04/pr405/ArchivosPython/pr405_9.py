palabras = ["sol", "luna", "estrella", "cielo", "mar"]

def obtener_longitud(pal):
    return len(pal)

longitudes = list(map(obtener_longitud, palabras))

diccionario = {}

for longitud in set(longitudes):
    def misma_longitud(palab):
        return len(palab) == longitud
    
    mismaLongitud = list(filter(misma_longitud, palabras))
    diccionario[longitud] = mismaLongitud

print(diccionario)
