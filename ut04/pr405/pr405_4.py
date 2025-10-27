palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

def letras(x):
    return len(x)>5

def mayus(x):
    return x.upper()

filt = filter(letras, palabras)
res = list(map(mayus, filt))
print(res)