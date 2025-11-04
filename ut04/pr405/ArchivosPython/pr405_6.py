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
