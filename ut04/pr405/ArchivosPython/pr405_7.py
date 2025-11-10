from functools import reduce

texto = "Hola hola mundo mundo cruel"

palabras = texto.lower().split()

pares = list(map(lambda x: (x, 1), palabras))

def acum(a, b):
    dic = a.copy()
    palabra, valor = b
    if palabra in dic:
        dic[palabra] += valor
    else:
        dic[palabra] = valor
    return dic

frecuencia = reduce(acum, pares, {})

print(frecuencia)
