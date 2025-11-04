# [UT04](./index.md)
# PR0404

## Ejercicio 1
```
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = []
numero = 0
def pares(x):
    for i in range(len(numeros)):
        return x%2 == 0

res = list(filter(pares, numeros)) 
print(res)
```

## Ejercicio 2
```
celsius = [0, 20, 37, 100]

def fah(x):
    return x*(9%5)+32

res = list(map(fah, celsius))

print(res)
```

## Ejercicio 3
```
numeros = [1, 2, 3, 4, 5]


def suma(x):
    x+=(x-1)

res = filter(suma, numeros)
print(res)

```

## Ejercicio 4
```
palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

def letras(x):
    return len(x)>5

def mayus(x):
    return x.upper()

filt = filter(letras, palabras)
res = list(map(mayus, filt))
print(res)
```

## Ejercicio 5
```
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]

pares = filter(lambda num: num % 2 == 0, numeros)
pares = map(lambda x: x, pares)

def multiplica(acum, num):
    return acum * num

res = reduce(multiplica, pares, 1)

print(res)
```

## Ejercicio 6
```
from functools import reduce
num = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]

def sumar(a, b):
    return a + b

def es_positivo(x):
    return x > 0

todos = []
for sublista in num:
    todos += sublista

posit = filter(es_positivo, todos)

suma = reduce(sumar, posit, 0)

print("La suma de todos los números positivos es:", suma)

```

## Ejercicio 9
```
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

```