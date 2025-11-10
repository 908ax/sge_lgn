from functools import reduce

funciones = [lambda x: x*2, lambda x: x+3, lambda x: x-1]
numeros = [1, 2, 3]

res = []

for i in numeros:
    r = reduce(lambda a, f: f(a), funciones, i)
    res.append(r)

print(res)
